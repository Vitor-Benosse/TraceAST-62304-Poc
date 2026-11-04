"""Comprehensive AST static analyzer and repository inspector for TraceAST-62304."""

from __future__ import annotations

import ast
import hashlib
import os
import re
import subprocess
import sys
import tomllib
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple
import yaml

from traceast.config import DEFAULT_EXCLUDED_DIRS, SENSITIVE_FILE_PATTERNS
from traceast.models import EvidenceItem

AI_ML_LIBRARIES: Dict[str, str] = {
    "torch": "PyTorch",
    "torchvision": "TorchVision",
    "torchaudio": "TorchAudio",
    "tensorflow": "TensorFlow",
    "keras": "Keras",
    "jax": "JAX",
    "flax": "Flax",
    "transformers": "Hugging Face Transformers",
    "diffusers": "Hugging Face Diffusers",
    "sklearn": "scikit-learn",
    "scikit-learn": "scikit-learn",
    "xgboost": "XGBoost",
    "lightgbm": "LightGBM",
    "catboost": "CatBoost",
    "onnx": "ONNX",
    "onnxruntime": "ONNX Runtime",
    "paddle": "PaddlePaddle",
    "mxnet": "Apache MXNet",
    "ultralytics": "Ultralytics",
    "cv2": "OpenCV",
    "opencv-python": "OpenCV",
    "sentence_transformers": "Sentence Transformers",
    "sentence-transformers": "Sentence Transformers",
    "monai": "MONAI (Medical Open Network for AI)",
    "pydicom": "PyDICOM",
    "nibabel": "NiBabel",
    "simpleitk": "SimpleITK",
}

PACKAGE_TO_IMPORT_MAP: Dict[str, str] = {
    "scikit-learn": "sklearn",
    "opencv-python": "cv2",
    "opencv-python-headless": "cv2",
    "pillow": "pil",
    "pyyaml": "yaml",
    "sentence-transformers": "sentence_transformers",
    "huggingface-hub": "huggingface_hub",
    "python-dotenv": "dotenv",
}

STDLIB_MODULES: Set[str] = set(sys.stdlib_module_names) if hasattr(sys, "stdlib_module_names") else {
    "os", "sys", "ast", "re", "json", "math", "pathlib", "typing", "logging", "unittest",
    "datetime", "collections", "itertools", "functools", "subprocess", "shutil", "tempfile",
    "hashlib", "csv", "io", "time", "argparse", "dataclasses", "enum", "abc", "copy", "pickle",
    "sqlite3", "urllib", "http", "asyncio", "concurrent", "threading", "multiprocessing", "warnings",
}

IO_CALL_NAMES: Set[str] = {
    "open",
    "read_text",
    "write_text",
    "read_bytes",
    "write_bytes",
    "read_csv",
    "to_csv",
    "read_excel",
    "to_excel",
    "read_parquet",
    "to_parquet",
    "read_json",
    "to_json",
    "dcmread",
    "SaveImage",
    "ReadImage",
    "imread",
    "imwrite",
    "load",
    "loads",
    "dump",
    "dumps",
}

MODEL_LOAD_CALLS: Set[str] = {
    "torch.load",
    "load_state_dict",
    "from_pretrained",
    "load_model",
    "joblib.load",
    "pickle.load",
    "onnx.load",
    "InferenceSession",
    "load_File",
    "load_checkpoint",
}

MODEL_SAVE_CALLS: Set[str] = {
    "torch.save",
    "save_pretrained",
    "save_model",
    "joblib.dump",
    "pickle.dump",
    "save_checkpoint",
    "to_onnx",
}

TRAINING_CALL_INDICATORS: Set[str] = {
    "backward",
    "step",
    "zero_grad",
    "fit",
    "train_on_batch",
}

INFERENCE_CALL_INDICATORS: Set[str] = {
    "eval",
    "no_grad",
    "inference_mode",
    "predict",
    "predict_proba",
    "generate",
}

MODEL_ARTIFACT_EXTENSIONS: Tuple[str, ...] = (
    ".pt",
    ".pth",
    ".onnx",
    ".h5",
    ".keras",
    ".pkl",
    ".joblib",
    ".safetensors",
    ".ckpt",
    ".pb",
)

VALIDATION_FUNCTION_KEYWORDS: Tuple[str, ...] = (
    "validate",
    "check",
    "verify",
    "sanitize",
    "schema",
    "assert",
    "clean",
)


def compute_sha256(file_path: Path) -> str:
    """Calculate SHA-256 hex digest of a file."""
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def get_git_commit_sha(repo_path: Path) -> Optional[str]:
    """Attempt to read the current Git commit SHA without modifying the repository."""
    git_dir = repo_path / ".git"
    if not git_dir.exists():
        return None
    try:
        head_file = git_dir / "HEAD"
        if head_file.exists():
            content = head_file.read_text(encoding="utf-8").strip()
            if content.startswith("ref: "):
                ref_path = git_dir / content[5:].strip()
                if ref_path.exists():
                    return ref_path.read_text(encoding="utf-8").strip()
            elif len(content) == 40:
                return content
        proc = subprocess.run(
            ["git", "-C", str(repo_path), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        if proc.returncode == 0:
            return proc.stdout.strip()
    except Exception:
        return None
    return None


def _get_call_name(node: ast.Call) -> str:
    """Resolve dotted name of an ast.Call target when possible."""
    func = node.func
    parts: List[str] = []
    while isinstance(func, ast.Attribute):
        parts.append(func.attr)
        func = func.value
    if isinstance(func, ast.Name):
        parts.append(func.id)
    parts.reverse()
    return ".".join(parts)


def _get_decorator_name(node: ast.expr) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        parts: List[str] = []
        curr: ast.expr = node
        while isinstance(curr, ast.Attribute):
            parts.append(curr.attr)
            curr = curr.value
        if isinstance(curr, ast.Name):
            parts.append(curr.id)
        parts.reverse()
        return ".".join(parts)
    if isinstance(node, ast.Call):
        return _get_call_name(node)
    return ast.dump(node)


def _is_empty_or_pass_handler(handler: ast.ExceptHandler) -> Tuple[bool, bool]:
    """Return (is_effectively_empty, uses_pass_statement)."""
    uses_pass = any(isinstance(stmt, ast.Pass) for stmt in handler.body)
    non_trivial = []
    for stmt in handler.body:
        if isinstance(stmt, ast.Pass):
            continue
        if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant):
            # Docstring or ellipsis `...` inside except block
            continue
        non_trivial.append(stmt)
    return (len(non_trivial) == 0, uses_pass)


def _format_exception_type(exc_expr: Optional[ast.expr]) -> List[str]:
    if exc_expr is None:
        return ["<bare_except>"]
    if isinstance(exc_expr, ast.Name):
        return [exc_expr.id]
    if isinstance(exc_expr, ast.Attribute):
        return [_get_decorator_name(exc_expr)]
    if isinstance(exc_expr, ast.Tuple):
        out: List[str] = []
        for elt in exc_expr.elts:
            out.extend(_format_exception_type(elt))
        return out
    return [ast.dump(exc_expr)]


class FileASTVisitor(ast.NodeVisitor):
    """Recursive AST visitor that tracks scope stack (classes, nested functions, async functions)."""

    def __init__(self, rel_path: str) -> None:
        self.rel_path = rel_path
        self.scope_stack: List[Tuple[str, str]] = []  # (kind, name)
        self.evidences: List[EvidenceItem] = []
        self.imports: Set[str] = set()
        self.classes: List[Dict[str, Any]] = []
        self.functions: List[Dict[str, Any]] = []
        self.try_blocks: List[Dict[str, Any]] = []
        self.io_operations: List[Dict[str, Any]] = []
        self.validation_signals: List[Dict[str, Any]] = []
        self.model_artifacts: List[Dict[str, Any]] = []
        self.training_signals: List[Dict[str, Any]] = []
        self.inference_signals: List[Dict[str, Any]] = []
        self.logging_calls: List[Dict[str, Any]] = []

    def current_symbol(self) -> Optional[str]:
        if not self.scope_stack:
            return None
        return ".".join(name for _, name in self.scope_stack)

    def _add_evidence(
        self,
        node: ast.AST,
        evidence_type: str,
        description: str,
        symbol_override: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> EvidenceItem:
        line_start = getattr(node, "lineno", 1) or 1
        line_end = getattr(node, "end_lineno", line_start) or line_start
        ev = EvidenceItem(
            file=self.rel_path,
            symbol=symbol_override if symbol_override is not None else self.current_symbol(),
            line_start=line_start,
            line_end=line_end,
            evidence_type=evidence_type,
            description=description,
            metadata=metadata or {},
        )
        self.evidences.append(ev)
        return ev

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            root_mod = alias.name.split(".")[0]
            self.imports.add(root_mod)
            self._add_evidence(
                node,
                evidence_type="ast_import",
                description=f"Importação de módulo '{alias.name}'",
                metadata={"module": alias.name, "root_module": root_mod},
            )
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        if node.module:
            root_mod = node.module.split(".")[0]
            self.imports.add(root_mod)
            imported_names = [a.name for a in node.names]
            self._add_evidence(
                node,
                evidence_type="ast_import_from",
                description=f"Importação a partir de '{node.module}': {', '.join(imported_names)}",
                metadata={"module": node.module, "root_module": root_mod, "names": imported_names},
            )
        self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        decorators = [_get_decorator_name(d) for d in node.decorator_list]
        bases = [_get_decorator_name(b) for b in node.bases]
        parent_symbol = self.current_symbol()
        full_name = f"{parent_symbol}.{node.name}" if parent_symbol else node.name
        class_info = {
            "name": node.name,
            "symbol": full_name,
            "line_start": node.lineno,
            "line_end": getattr(node, "end_lineno", node.lineno),
            "decorators": decorators,
            "bases": bases,
        }
        self.classes.append(class_info)
        self._add_evidence(
            node,
            evidence_type="ast_class",
            description=f"Definição de classe '{full_name}' (bases: {', '.join(bases) or 'nenhuma'})",
            symbol_override=full_name,
            metadata=class_info,
        )
        self.scope_stack.append(("class", node.name))
        self.generic_visit(node)
        self.scope_stack.pop()

    def _handle_function(self, node: ast.FunctionDef | ast.AsyncFunctionDef, is_async: bool) -> None:
        parent_kind = self.scope_stack[-1][0] if self.scope_stack else None
        is_method = parent_kind == "class"
        is_nested = parent_kind is not None and parent_kind != "class"
        if is_method:
            func_kind = "async_method" if is_async else "method"
        elif is_nested:
            func_kind = "nested_async_function" if is_async else "nested_function"
        else:
            func_kind = "async_function" if is_async else "top_level_function"

        parent_symbol = self.current_symbol()
        full_name = f"{parent_symbol}.{node.name}" if parent_symbol else node.name
        decorators = [_get_decorator_name(d) for d in node.decorator_list]
        args_list = [a.arg for a in node.args.args]
        has_type_annotations = any(a.annotation is not None for a in node.args.args) or (node.returns is not None)

        # Inspect direct statements/subnodes for local try-except presence
        has_try_block = any(isinstance(child, ast.Try) for child in ast.walk(node))

        func_info = {
            "name": node.name,
            "symbol": full_name,
            "kind": func_kind,
            "is_async": is_async,
            "is_nested": is_nested,
            "is_method": is_method,
            "line_start": node.lineno,
            "line_end": getattr(node, "end_lineno", node.lineno),
            "decorators": decorators,
            "args": args_list,
            "has_type_annotations": has_type_annotations,
            "has_try_block": has_try_block,
        }
        self.functions.append(func_info)
        self._add_evidence(
            node,
            evidence_type=f"ast_{func_kind}",
            description=f"Definição de {func_kind} '{full_name}' (decoradores: {', '.join(decorators) or 'nenhum'})",
            symbol_override=full_name,
            metadata=func_info,
        )

        lower_name = node.name.lower()
        if any(k in lower_name for k in VALIDATION_FUNCTION_KEYWORDS):
            val_item = {
                "symbol": full_name,
                "line_start": node.lineno,
                "line_end": getattr(node, "end_lineno", node.lineno),
                "signal_type": "validation_function_definition",
                "detail": f"Função de validação candidata '{full_name}'",
            }
            self.validation_signals.append(val_item)
            self._add_evidence(
                node,
                evidence_type="ast_input_validation",
                description=f"Função candidata a validação de entrada '{full_name}'",
                symbol_override=full_name,
                metadata=val_item,
            )

        if any(k in lower_name for k in ("train", "fit_model", "fine_tune", "finetune")):
            tr_item = {
                "symbol": full_name,
                "line_start": node.lineno,
                "line_end": getattr(node, "end_lineno", node.lineno),
                "signal_type": "training_function",
                "detail": f"Função associada a treinamento '{full_name}'",
            }
            self.training_signals.append(tr_item)
            self._add_evidence(
                node,
                evidence_type="ast_training_signal",
                description=f"Função associada a rotina de treinamento '{full_name}'",
                symbol_override=full_name,
                metadata=tr_item,
            )

        if lower_name == "forward" or any(
            k in lower_name for k in ("predict", "infer", "inference", "generate_report", "diagnose")
        ):
            inf_item = {
                "symbol": full_name,
                "line_start": node.lineno,
                "line_end": getattr(node, "end_lineno", node.lineno),
                "signal_type": "inference_function",
                "detail": f"Função/método associado a inferência ou passagem direta '{full_name}'",
            }
            self.inference_signals.append(inf_item)
            self._add_evidence(
                node,
                evidence_type="ast_inference_signal",
                description=f"Função/método associado a inferência '{full_name}'",
                symbol_override=full_name,
                metadata=inf_item,
            )

        self.scope_stack.append((func_kind, node.name))
        self.generic_visit(node)
        self.scope_stack.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self._handle_function(node, is_async=False)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self._handle_function(node, is_async=True)

    def visit_Try(self, node: ast.Try) -> None:
        handlers_meta: List[Dict[str, Any]] = []
        has_empty_handler = False
        has_pass_handler = False
        all_exc_types: List[str] = []

        for h in node.handlers:
            exc_types = _format_exception_type(h.type)
            all_exc_types.extend(exc_types)
            is_empty, uses_pass = _is_empty_or_pass_handler(h)
            if is_empty:
                has_empty_handler = True
            if uses_pass:
                has_pass_handler = True
            handlers_meta.append(
                {
                    "exception_types": exc_types,
                    "is_empty": is_empty,
                    "uses_pass": uses_pass,
                    "line_start": h.lineno,
                    "line_end": getattr(h, "end_lineno", h.lineno),
                }
            )

        try_meta = {
            "symbol": self.current_symbol(),
            "line_start": node.lineno,
            "line_end": getattr(node, "end_lineno", node.lineno),
            "exception_types": all_exc_types,
            "has_finally": len(node.finalbody) > 0,
            "has_else": len(node.orelse) > 0,
            "has_empty_except": has_empty_handler,
            "has_pass_in_except": has_pass_handler,
            "handlers": handlers_meta,
        }
        self.try_blocks.append(try_meta)
        self._add_evidence(
            node,
            evidence_type="ast_try_except",
            description=(
                f"Bloco try-except (exceções: {', '.join(all_exc_types) or 'nenhuma'}; "
                f"finally: {len(node.finalbody) > 0}; except vazio/pass: {has_empty_handler or has_pass_handler})"
            ),
            metadata=try_meta,
        )
        self.generic_visit(node)

    def visit_Assert(self, node: ast.Assert) -> None:
        val_item = {
            "symbol": self.current_symbol(),
            "line_start": node.lineno,
            "line_end": getattr(node, "end_lineno", node.lineno),
            "signal_type": "assert_statement",
            "detail": "Instrução assert encontrada",
        }
        self.validation_signals.append(val_item)
        self._add_evidence(
            node,
            evidence_type="ast_input_validation",
            description=f"Verificação por assert em '{self.current_symbol() or '<module>'}'",
            metadata=val_item,
        )
        self.generic_visit(node)

    def visit_If(self, node: ast.If) -> None:
        # Detect conditional input validation patterns (e.g. if ... raise ValueError/TypeError)
        raises_validation_error = any(
            isinstance(stmt, ast.Raise) for stmt in node.body
        )
        test_dump = ast.dump(node.test)
        checks_type_or_none = "isinstance" in test_dump or "Constant(value=None)" in test_dump
        if raises_validation_error or checks_type_or_none:
            val_item = {
                "symbol": self.current_symbol(),
                "line_start": node.lineno,
                "line_end": getattr(node, "end_lineno", node.lineno),
                "signal_type": "conditional_guard",
                "raises_exception": raises_validation_error,
                "checks_type_or_none": checks_type_or_none,
            }
            self.validation_signals.append(val_item)
            self._add_evidence(
                node,
                evidence_type="ast_conditional_guard",
                description=(
                    f"Estrutura condicional relevante em '{self.current_symbol() or '<module>'}' "
                    f"(levanta exceção: {raises_validation_error}, verifica tipo/None: {checks_type_or_none})"
                ),
                metadata=val_item,
            )
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        call_name = _get_call_name(node)
        short_name = call_name.split(".")[-1] if call_name else ""
        symbol = self.current_symbol()

        # Check if inside a try block by line range
        in_try = any(
            tb["line_start"] <= node.lineno <= tb["line_end"]
            for tb in self.try_blocks
        )
        in_non_empty_try = any(
            tb["line_start"] <= node.lineno <= tb["line_end"] and not tb["has_empty_except"]
            for tb in self.try_blocks
        )

        # 1. Logging calls
        if call_name.startswith(("logging.", "logger.", "log.")) or short_name in {
            "debug", "info", "warning", "error", "critical", "exception"
        } and any(p in call_name for p in ("log", "logger", "logging")):
            log_item = {
                "call": call_name,
                "symbol": symbol,
                "line_start": node.lineno,
                "line_end": getattr(node, "end_lineno", node.lineno),
            }
            self.logging_calls.append(log_item)
            self._add_evidence(
                node,
                evidence_type="ast_logging_call",
                description=f"Chamada de logging '{call_name}'",
                metadata=log_item,
            )

        # 2. I/O calls
        if short_name in IO_CALL_NAMES or call_name in MODEL_LOAD_CALLS or call_name in MODEL_SAVE_CALLS:
            io_item = {
                "call": call_name,
                "symbol": symbol,
                "line_start": node.lineno,
                "line_end": getattr(node, "end_lineno", node.lineno),
                "inside_try_block": in_try,
                "inside_non_empty_try": in_non_empty_try,
            }
            self.io_operations.append(io_item)
            self._add_evidence(
                node,
                evidence_type="ast_io_call",
                description=(
                    f"Operação de I/O '{call_name}' em '{symbol or '<module>'}' "
                    f"(protegida por try-except: {in_try})"
                ),
                metadata=io_item,
            )

        # 3. Model loading / saving & provenance calls
        if call_name in MODEL_LOAD_CALLS or short_name in {"load_state_dict", "from_pretrained", "load_model"}:
            art_item = {
                "call": call_name,
                "action": "model_load",
                "symbol": symbol,
                "line_start": node.lineno,
                "line_end": getattr(node, "end_lineno", node.lineno),
            }
            self.model_artifacts.append(art_item)
            self._add_evidence(
                node,
                evidence_type="ast_model_load",
                description=f"Carregamento de modelo/artefato via '{call_name}'",
                metadata=art_item,
            )

        if call_name in MODEL_SAVE_CALLS or short_name in {"save_pretrained", "save_model", "save_checkpoint"}:
            art_item = {
                "call": call_name,
                "action": "model_save",
                "symbol": symbol,
                "line_start": node.lineno,
                "line_end": getattr(node, "end_lineno", node.lineno),
            }
            self.model_artifacts.append(art_item)
            self._add_evidence(
                node,
                evidence_type="ast_model_save",
                description=f"Salvamento de modelo/artefato via '{call_name}'",
                metadata=art_item,
            )

        # 4. Training calls
        if short_name in TRAINING_CALL_INDICATORS or call_name.endswith(".train"):
            tr_item = {
                "call": call_name,
                "symbol": symbol,
                "line_start": node.lineno,
                "line_end": getattr(node, "end_lineno", node.lineno),
                "signal_type": "training_call",
            }
            self.training_signals.append(tr_item)
            self._add_evidence(
                node,
                evidence_type="ast_training_call",
                description=f"Chamada associada a treinamento '{call_name}' em '{symbol or '<module>'}'",
                metadata=tr_item,
            )

        # 5. Inference calls
        if short_name in INFERENCE_CALL_INDICATORS:
            inf_item = {
                "call": call_name,
                "symbol": symbol,
                "line_start": node.lineno,
                "line_end": getattr(node, "end_lineno", node.lineno),
                "signal_type": "inference_call",
            }
            self.inference_signals.append(inf_item)
            self._add_evidence(
                node,
                evidence_type="ast_inference_call",
                description=f"Chamada associada a inferência '{call_name}' em '{symbol or '<module>'}'",
                metadata=inf_item,
            )

        # 6. Validation calls (isinstance, pydantic validate, etc.)
        if short_name in {"isinstance", "issubclass", "model_validate", "parse_obj", "validate"}:
            val_item = {
                "call": call_name,
                "symbol": symbol,
                "line_start": node.lineno,
                "line_end": getattr(node, "end_lineno", node.lineno),
                "signal_type": "validation_call",
            }
            self.validation_signals.append(val_item)
            self._add_evidence(
                node,
                evidence_type="ast_validation_call",
                description=f"Chamada de verificação/validação '{call_name}' em '{symbol or '<module>'}'",
                metadata=val_item,
            )

        # 7. Check string arguments for model checkpoint references (.pt, .pth, .onnx, etc.)
        for arg in node.args:
            if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                val_str = arg.value.lower()
                if val_str.endswith(MODEL_ARTIFACT_EXTENSIONS):
                    ckpt_item = {
                        "artifact_reference": arg.value,
                        "call": call_name,
                        "symbol": symbol,
                        "line_start": node.lineno,
                        "line_end": getattr(node, "end_lineno", node.lineno),
                        "action": "checkpoint_reference",
                    }
                    self.model_artifacts.append(ckpt_item)
                    self._add_evidence(
                        node,
                        evidence_type="ast_checkpoint_reference",
                        description=f"Referência a artefato/checkpoint de modelo '{arg.value}' em '{call_name}'",
                        metadata=ckpt_item,
                    )

        self.generic_visit(node)


def parse_dependencies_from_repo(repo_path: Path, imported_modules: Set[str]) -> Dict[str, Any]:
    """Inspect dependency files (requirements.txt, pyproject.toml, poetry.lock, setup.py) without executing code."""
    dep_files_found: List[str] = []
    declared_dependencies: List[Dict[str, Any]] = []
    evidences: List[EvidenceItem] = []

    req_pattern = re.compile(r"^([A-Za-z0-9_.\-]+)\s*(\[[^\]]+\])?\s*([<>=!~]=?.*)?$")

    for req_file in sorted(repo_path.rglob("*requirements*.txt")):
        rel_parts = set(req_file.relative_to(repo_path).parts)
        if rel_parts & DEFAULT_EXCLUDED_DIRS:
            continue
        rel_path = req_file.relative_to(repo_path).as_posix()
        dep_files_found.append(rel_path)
        try:
            lines = req_file.read_text(encoding="utf-8", errors="replace").splitlines()
            for idx, raw_line in enumerate(lines, start=1):
                line = raw_line.split("#", 1)[0].strip()
                if not line or line.startswith(("-", "git+", "http:", "https:")):
                    continue
                m = req_pattern.match(line)
                if m:
                    pkg_name = m.group(1).strip()
                    version_spec = (m.group(3) or "").strip()
                    is_pinned = version_spec.startswith("==") and "*" not in version_spec
                    norm_pkg = pkg_name.lower()
                    import_alias = PACKAGE_TO_IMPORT_MAP.get(norm_pkg, norm_pkg.replace("-", "_"))
                    is_used = import_alias in {m_name.lower() for m_name in imported_modules}
                    is_ai = norm_pkg in AI_ML_LIBRARIES or import_alias in AI_ML_LIBRARIES
                    dep_entry = {
                        "package": pkg_name,
                        "version_spec": version_spec or None,
                        "is_pinned": is_pinned,
                        "is_imported_in_code": is_used,
                        "is_ai_ml_component": is_ai,
                        "source_file": rel_path,
                        "line": idx,
                    }
                    declared_dependencies.append(dep_entry)
                    evidences.append(
                        EvidenceItem(
                            file=rel_path,
                            symbol=pkg_name,
                            line_start=idx,
                            line_end=idx,
                            evidence_type="dependency_declaration",
                            description=(
                                f"Dependência '{pkg_name}' (versão: '{version_spec or 'não especificada'}', "
                                f"fixada: {is_pinned}, importada no código: {is_used})"
                            ),
                            metadata=dep_entry,
                        )
                    )
        except Exception:
            pass

    pyproject_file = repo_path / "pyproject.toml"
    if pyproject_file.exists():
        rel_path = "pyproject.toml"
        dep_files_found.append(rel_path)
        try:
            content = pyproject_file.read_text(encoding="utf-8", errors="replace")
            data = tomllib.loads(content)
            proj_deps = data.get("project", {}).get("dependencies", [])
            for dep_str in proj_deps:
                m = req_pattern.match(str(dep_str).strip())
                if m:
                    pkg_name = m.group(1).strip()
                    version_spec = (m.group(3) or "").strip()
                    is_pinned = version_spec.startswith("==") and "*" not in version_spec
                    norm_pkg = pkg_name.lower()
                    import_alias = PACKAGE_TO_IMPORT_MAP.get(norm_pkg, norm_pkg.replace("-", "_"))
                    is_used = import_alias in {m_name.lower() for m_name in imported_modules}
                    is_ai = norm_pkg in AI_ML_LIBRARIES or import_alias in AI_ML_LIBRARIES
                    dep_entry = {
                        "package": pkg_name,
                        "version_spec": version_spec or None,
                        "is_pinned": is_pinned,
                        "is_imported_in_code": is_used,
                        "is_ai_ml_component": is_ai,
                        "source_file": rel_path,
                        "line": 1,
                    }
                    declared_dependencies.append(dep_entry)
                    evidences.append(
                        EvidenceItem(
                            file=rel_path,
                            symbol=pkg_name,
                            line_start=1,
                            line_end=1,
                            evidence_type="dependency_declaration",
                            description=(
                                f"Dependência em pyproject.toml '{pkg_name}' "
                                f"(versão: '{version_spec or 'não especificada'}', fixada: {is_pinned})"
                            ),
                            metadata=dep_entry,
                        )
                    )
            poetry_deps = data.get("tool", {}).get("poetry", {}).get("dependencies", {})
            for pkg_name, spec in poetry_deps.items():
                if pkg_name.lower() == "python":
                    continue
                version_spec = str(spec) if not isinstance(spec, dict) else str(spec.get("version", ""))
                is_pinned = bool(re.match(r"^\d+\.\d+\.\d+$", version_spec.strip("= ")))
                norm_pkg = pkg_name.lower()
                import_alias = PACKAGE_TO_IMPORT_MAP.get(norm_pkg, norm_pkg.replace("-", "_"))
                is_used = import_alias in {m_name.lower() for m_name in imported_modules}
                is_ai = norm_pkg in AI_ML_LIBRARIES or import_alias in AI_ML_LIBRARIES
                dep_entry = {
                    "package": pkg_name,
                    "version_spec": version_spec or None,
                    "is_pinned": is_pinned,
                    "is_imported_in_code": is_used,
                    "is_ai_ml_component": is_ai,
                    "source_file": rel_path,
                    "line": 1,
                }
                declared_dependencies.append(dep_entry)
                evidences.append(
                    EvidenceItem(
                        file=rel_path,
                        symbol=pkg_name,
                        line_start=1,
                        line_end=1,
                        evidence_type="dependency_declaration",
                        description=f"Dependência Poetry '{pkg_name}' ({version_spec})",
                        metadata=dep_entry,
                    )
                )
        except Exception:
            pass

    poetry_lock = repo_path / "poetry.lock"
    if poetry_lock.exists():
        dep_files_found.append("poetry.lock")
        evidences.append(
            EvidenceItem(
                file="poetry.lock",
                symbol="poetry.lock",
                line_start=1,
                line_end=1,
                evidence_type="dependency_lockfile",
                description="Arquivo de bloqueio de versões poetry.lock identificado.",
            )
        )

    # Identify third-party imports in code that were not declared
    declared_import_names = {
        PACKAGE_TO_IMPORT_MAP.get(d["package"].lower(), d["package"].lower().replace("-", "_"))
        for d in declared_dependencies
    }
    undeclared_imports: List[str] = []
    for imp in sorted(imported_modules):
        imp_low = imp.lower()
        if imp_low in STDLIB_MODULES or imp_low.startswith("_"):
            continue
        # Exclude internal modules present in repo
        if (repo_path / f"{imp}.py").exists() or (repo_path / imp).is_dir():
            continue
        if imp_low not in declared_import_names:
            undeclared_imports.append(imp)

    pinned_count = sum(1 for d in declared_dependencies if d["is_pinned"])
    unpinned_count = sum(1 for d in declared_dependencies if not d["is_pinned"])
    ai_components = sorted(
        {
            AI_ML_LIBRARIES.get(d["package"].lower(), d["package"])
            for d in declared_dependencies
            if d["is_ai_ml_component"]
        }
        | {
            AI_ML_LIBRARIES[imp.lower()]
            for imp in imported_modules
            if imp.lower() in AI_ML_LIBRARIES
        }
    )

    return {
        "dependency_files": dep_files_found,
        "declared_dependencies": declared_dependencies,
        "pinned_count": pinned_count,
        "unpinned_count": unpinned_count,
        "undeclared_third_party_imports": undeclared_imports,
        "ai_ml_components": ai_components,
        "evidences": evidences,
    }


def inspect_tests_and_ci(
    repo_path: Path,
    parsed_files_data: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Identify test directories, test files, frameworks, CI/CD workflows, and test commands."""
    test_dirs: List[str] = []
    test_files: List[str] = []
    test_frameworks: Set[str] = set()
    test_configs: List[str] = []
    ci_workflows: List[Dict[str, Any]] = []
    coverage_evidences: List[str] = []
    evidences: List[EvidenceItem] = []

    for candidate_dir in ("tests", "test", "unit_tests", "integration_tests"):
        d_path = repo_path / candidate_dir
        if d_path.exists() and d_path.is_dir():
            test_dirs.append(candidate_dir)

    for cfg_name in ("pytest.ini", "tox.ini", ".coveragerc", "setup.cfg"):
        if (repo_path / cfg_name).exists():
            test_configs.append(cfg_name)
            if cfg_name == ".coveragerc":
                coverage_evidences.append(cfg_name)

    for f_data in parsed_files_data:
        rel_path = f_data["file"]
        fname = Path(rel_path).name
        parts = Path(rel_path).parts
        is_test_file = (
            fname.startswith("test_")
            or fname.endswith("_test.py")
            or any(p in {"tests", "test"} for p in parts)
        )
        if is_test_file:
            test_files.append(rel_path)
            if "pytest" in f_data["imports"]:
                test_frameworks.add("pytest")
            if "unittest" in f_data["imports"]:
                test_frameworks.add("unittest")
            test_funcs = [
                fn for fn in f_data["functions"] if fn["name"].startswith("test_") or fn["is_method"]
            ]
            evidences.append(
                EvidenceItem(
                    file=rel_path,
                    symbol=test_funcs[0]["symbol"] if test_funcs else None,
                    line_start=test_funcs[0]["line_start"] if test_funcs else 1,
                    line_end=test_funcs[0]["line_end"] if test_funcs else 1,
                    evidence_type="test_file",
                    description=f"Arquivo de teste identificado '{rel_path}' ({len(test_funcs)} funções/métodos de teste)",
                    metadata={"test_functions_count": len(test_funcs)},
                )
            )

    # Check GitHub Actions and GitLab CI workflows
    gh_workflows_dir = repo_path / ".github" / "workflows"
    if gh_workflows_dir.exists() and gh_workflows_dir.is_dir():
        for wf_file in sorted(list(gh_workflows_dir.glob("*.yml")) + list(gh_workflows_dir.glob("*.yaml"))):
            rel_wf = wf_file.relative_to(repo_path).as_posix()
            raw_text = wf_file.read_text(encoding="utf-8", errors="replace")
            test_cmds: List[str] = []
            has_cov = False
            for idx, line in enumerate(raw_text.splitlines(), start=1):
                stripped = line.strip()
                if any(tok in stripped for tok in ("pytest", "unittest", "tox", "coverage run")):
                    test_cmds.append(stripped)
                    if "--cov" in stripped or "coverage" in stripped:
                        has_cov = True
                        coverage_evidences.append(f"{rel_wf}:{idx}")
                    evidences.append(
                        EvidenceItem(
                            file=rel_wf,
                            symbol="ci_test_step",
                            line_start=idx,
                            line_end=idx,
                            evidence_type="ci_test_command",
                            description=f"Comando de teste em workflow CI '{rel_wf}': {stripped}",
                            metadata={"command": stripped, "has_coverage": has_cov},
                        )
                    )
            if not test_cmds:
                evidences.append(
                    EvidenceItem(
                        file=rel_wf,
                        symbol="ci_workflow",
                        line_start=1,
                        line_end=1,
                        evidence_type="ci_workflow_file",
                        description=f"Workflow CI '{rel_wf}' identificado sem comando explícito de teste Python.",
                    )
                )
            ci_workflows.append(
                {
                    "file": rel_wf,
                    "test_commands": test_cmds,
                    "has_coverage": has_cov,
                }
            )

    gitlab_ci = repo_path / ".gitlab-ci.yml"
    if gitlab_ci.exists():
        raw_text = gitlab_ci.read_text(encoding="utf-8", errors="replace")
        test_cmds = [
            line.strip()
            for line in raw_text.splitlines()
            if any(tok in line for tok in ("pytest", "unittest", "coverage"))
        ]
        ci_workflows.append(
            {
                "file": ".gitlab-ci.yml",
                "test_commands": test_cmds,
                "has_coverage": any("cov" in c for c in test_cmds),
            }
        )
        evidences.append(
            EvidenceItem(
                file=".gitlab-ci.yml",
                symbol="gitlab_ci",
                line_start=1,
                line_end=1,
                evidence_type="ci_workflow_file",
                description=f"Configuração GitLab CI identificada (comandos de teste: {len(test_cmds)}).",
            )
        )

    return {
        "test_directories": test_dirs,
        "test_files": test_files,
        "test_frameworks": sorted(test_frameworks),
        "test_configs": test_configs,
        "ci_workflows": ci_workflows,
        "coverage_evidences": coverage_evidences,
        "evidences": evidences,
    }


def analyze_repository_static(
    repo_path: Path,
    excluded_dirs: Optional[Set[str]] = None,
) -> Dict[str, Any]:
    """Perform complete static AST and structural inspection of a target repository without executing code."""
    repo_path = Path(repo_path).resolve()
    if not repo_path.exists() or not repo_path.is_dir():
        raise FileNotFoundError(f"Repository directory does not exist: {repo_path}")

    active_excludes = set(DEFAULT_EXCLUDED_DIRS) | (excluded_dirs or set())

    total_files_found = 0
    excluded_sensitive_files: List[str] = []
    python_files_found: List[Path] = []
    standalone_model_files: List[str] = []

    for root, dirs, files in os.walk(repo_path):
        # Prune excluded directories in-place
        dirs[:] = sorted([d for d in dirs if d not in active_excludes])
        for fname in sorted(files):
            if fname in SENSITIVE_FILE_PATTERNS or fname.startswith(".env"):
                rel_s = (Path(root) / fname).relative_to(repo_path).as_posix()
                excluded_sensitive_files.append(rel_s)
                continue
            total_files_found += 1
            full_path = Path(root) / fname
            if fname.endswith(".py"):
                python_files_found.append(full_path)
            elif fname.lower().endswith(MODEL_ARTIFACT_EXTENSIONS):
                standalone_model_files.append(full_path.relative_to(repo_path).as_posix())

    parsed_files: List[Dict[str, Any]] = []
    failed_files: List[Dict[str, Any]] = []
    all_evidences: List[EvidenceItem] = []
    all_imports: Set[str] = set()

    for py_file in python_files_found:
        rel_path = py_file.relative_to(repo_path).as_posix()
        try:
            file_hash = compute_sha256(py_file)
        except Exception as e:
            failed_files.append(
                {
                    "file": rel_path,
                    "sha256": None,
                    "error_type": type(e).__name__,
                    "reason": f"Falha de leitura binária/permissão: {e}",
                    "line": None,
                }
            )
            continue

        try:
            raw_bytes = py_file.read_bytes()
            source_text = raw_bytes.decode("utf-8-sig")
        except UnicodeDecodeError as e:
            failed_files.append(
                {
                    "file": rel_path,
                    "sha256": file_hash,
                    "error_type": "UnicodeDecodeError",
                    "reason": f"Erro de decodificação UTF-8 na posição {e.start}: {e.reason}",
                    "line": None,
                }
            )
            continue

        try:
            tree = ast.parse(source_text, filename=rel_path)
        except SyntaxError as e:
            failed_files.append(
                {
                    "file": rel_path,
                    "sha256": file_hash,
                    "error_type": "SyntaxError",
                    "reason": f"Erro de sintaxe Python na linha {e.lineno}: {e.msg}",
                    "line": e.lineno,
                }
            )
            continue
        except Exception as e:
            failed_files.append(
                {
                    "file": rel_path,
                    "sha256": file_hash,
                    "error_type": type(e).__name__,
                    "reason": f"Erro inesperado ao analisar AST: {e}",
                    "line": None,
                }
            )
            continue

        visitor = FileASTVisitor(rel_path)
        visitor.visit(tree)
        all_imports.update(visitor.imports)
        all_evidences.extend(visitor.evidences)

        line_count = max(1, len(source_text.splitlines()))
        parsed_files.append(
            {
                "file": rel_path,
                "sha256": file_hash,
                "line_count": line_count,
                "imports": sorted(visitor.imports),
                "classes": visitor.classes,
                "functions": visitor.functions,
                "try_blocks": visitor.try_blocks,
                "io_operations": visitor.io_operations,
                "validation_signals": visitor.validation_signals,
                "model_artifacts": visitor.model_artifacts,
                "training_signals": visitor.training_signals,
                "inference_signals": visitor.inference_signals,
                "logging_calls": visitor.logging_calls,
            }
        )

    for mf in standalone_model_files:
        all_evidences.append(
            EvidenceItem(
                file=mf,
                symbol=Path(mf).name,
                line_start=1,
                line_end=1,
                evidence_type="standalone_model_artifact",
                description=f"Arquivo de artefato/checkpoint de modelo presente no repositório: '{mf}'",
            )
        )

    dep_report = parse_dependencies_from_repo(repo_path, all_imports)
    all_evidences.extend(dep_report["evidences"])

    test_ci_report = inspect_tests_and_ci(repo_path, parsed_files)
    all_evidences.extend(test_ci_report["evidences"])

    total_py = len(python_files_found)
    success_py = len(parsed_files)
    failed_py = len(failed_files)
    coverage_pct = round((success_py / total_py) * 100.0, 2) if total_py > 0 else 0.0

    return {
        "repository_path": str(repo_path),
        "commit_sha": get_git_commit_sha(repo_path),
        "python_version": sys.version.split()[0],
        "inspection_summary": {
            "total_files_found": total_files_found,
            "python_files_found": total_py,
            "python_files_parsed_successfully": success_py,
            "python_files_failed": failed_py,
            "inspection_coverage_percent": coverage_pct,
            "excluded_sensitive_files_count": len(excluded_sensitive_files),
        },
        "parsed_files": parsed_files,
        "failed_files": failed_files,
        "standalone_model_files": standalone_model_files,
        "dependencies": {k: v for k, v in dep_report.items() if k != "evidences"},
        "tests_and_ci": {k: v for k, v in test_ci_report.items() if k != "evidences"},
        "all_evidences": [ev.model_dump() for ev in all_evidences],
    }

