import os
import ast
import subprocess
import shutil
import argparse
from pathlib import Path
import tempfile
import stat

clone_dir = Path(tempfile.gettempdir()) / "repo_temp"

AI_FRAMEWORKS = {
    "torch": "PyTorch",
    "tensorflow": "TensorFlow",
    "keras": "Keras",
    "jax": "JAX",
    "flax": "Flax",
    "transformers": "Hugging Face Transformers",
    "diffusers": "Hugging Face Diffusers",
    "sklearn": "scikit-learn",
    "xgboost": "XGBoost",
    "lightgbm": "LightGBM",
    "catboost": "CatBoost",
    "onnx": "ONNX",
    "paddle": "PaddlePaddle",
    "mxnet": "Apache MXNet",
    "ultralytics": "Ultralytics",
    "cv2": "OpenCV",
    "sentence_transformers": "Sentence Transformers",
}

def remove_read_only(func, path, exc):
    if isinstance(exc, PermissionError):
        os.chmod(path, stat.S_IWRITE | stat.S_IREAD)
        func(path)
    else:
        raise exc

def parse_python_file(file_path):
    """
    Parses a Python file and returns a string with the extracted AST semantics.
    """
    output_lines = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
    except Exception as e:
        return f"\n[WARNING] Was not possible to read: {file_path}: {e}"

    output_lines.append(f"\n{'='*60}\nFile: {file_path}\n{'='*60}")

    imported_modules = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_modules.update(alias.name.split('.')[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_modules.add(node.module.split('.')[0])

    frameworks = sorted({
        framework
        for module, framework in AI_FRAMEWORKS.items()
        if module in imported_modules
    })
    if frameworks:
        output_lines.append(f"\n[AI FRAMEWORKS] {', '.join(frameworks)}")

    # Keywords to identify patient data flow (I/O)
    io_keywords = ["load", "save", "preprocess", "read", "write", "import", "export"]

    # Run through the AST nodes to find classes and functions
    for node in tree.body:
        # If it's a class definition, append its name and docstring
        if isinstance(node, ast.ClassDef):
            output_lines.append(f"\n[CLASS] {node.name}")
            doc = ast.get_docstring(node)
            if doc:
                indent_doc = doc.replace('\n', '\n    ')
                output_lines.append(f"  Class docstring:\n    {indent_doc}")

            # Check for methods inside the class
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    # 1. Network Architecture Extraction
                    if item.name == "forward":
                        output_lines.append(f"  [NETWORK ARCHITECTURE] {item.name}")
                    else:
                        output_lines.append(f"  [METHOD] {item.name}")
                    
                    fdoc = ast.get_docstring(item)
                    if fdoc:
                        indent_fdoc = fdoc.replace('\n', '\n      ')
                        output_lines.append(f"    Docstring:\n      {indent_fdoc}")
                    
                    # 2. Safeguards Extraction (try...except)
                    for child in ast.walk(item):
                        if isinstance(child, ast.Try):
                            handlers = [h.type.id if getattr(h.type, 'id', None) else "Exception" for h in child.handlers]
                            output_lines.append(f"    [SAFEGUARD] try...except block found (Handlers: {', '.join(handlers)})")

        # If it's a standalone function
        elif isinstance(node, ast.FunctionDef):
            # 3. Data Flow Extraction (I/O)
            is_io = any(kw in node.name.lower() for kw in io_keywords)
            if is_io:
                output_lines.append(f"\n[I/O FUNCTION] {node.name}")
            else:
                output_lines.append(f"\n[FUNCTION] {node.name}")
            
            doc = ast.get_docstring(node)
            if doc:
                indent_doc = doc.replace('\n', '\n    ')
                output_lines.append(f"  Docstring:\n    {indent_doc}")

            # 2. Safeguards Extraction (try...except) in standalone functions
            for child in ast.walk(node):
                if isinstance(child, ast.Try):
                    handlers = [h.type.id if getattr(h.type, 'id', None) else "Exception" for h in child.handlers]
                    output_lines.append(f"  [SAFEGUARD] try...except block found (Handlers: {', '.join(handlers)})")

    return "\n".join(output_lines)

def analyze_repository(repo_url, clone_dir):
    """ 
    Clone git repository, analyze (.py) files and return the full AST report as a string.
    """
    full_ast_report = []
    
    # Clean up the clone directory if it already exists
    if clone_dir.exists():
        print(f"Removing old directory: {clone_dir}")
        shutil.rmtree(clone_dir, onexc=remove_read_only)

    print(f"\nCloning repository: {repo_url}...")
    
    # git clone with error handling
    try:
        subprocess.run(["git", "clone", repo_url, clone_dir], check=True)
        print("Clone completed. Starting analysis...\n")
    except subprocess.CalledProcessError as e:
        error_msg = f"\n[ERROR] Could not clone the repository. Please check if the URL is correct or if the repository is public: {e}"
        print(error_msg)
        return error_msg

    # Run through all folders and files in the cloned repository
    for root, _, files in os.walk(clone_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                file_ast = parse_python_file(file_path)
                if file_ast:
                    full_ast_report.append(file_ast)
                    
    return "\n".join(full_ast_report)

def main():
    parser = argparse.ArgumentParser(description="Analyze Python files in a Git repository.")
    parser.add_argument(
        "repo_url",
        nargs="?",
        default="https://github.com/anandr07/Medical-Report-Generator-from-Chest-X-Ray-Images",
        help="URL of the Git repository to be analyzed",
    )
    args = parser.parse_args()
    
    # Prints the extracted AST structure via terminal or provides the string for local PoC auditing.
    final_report = analyze_repository(args.repo_url, clone_dir)
    print(final_report)

if __name__ == "__main__":
    main()