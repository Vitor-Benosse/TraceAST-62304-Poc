"""Deterministic rule evaluation engine for TraceAST-62304 (Rules R01 through R08)."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional

from traceast.models import (
    ConfidenceLevel,
    EvidenceItem,
    Finding,
    FindingStatus,
    ProductProfile,
    ReviewPriority,
    RuleDefinition,
)
from traceast.rule_catalog import get_rule_catalog_dict

STATUS_LABELS_PT: Dict[FindingStatus, str] = {
    FindingStatus.OBSERVED: "Evidência identificada",
    FindingStatus.NOT_OBSERVED: "Evidência não identificada no repositório analisado",
    FindingStatus.PARTIAL: "Evidência parcial — indicador técnico que merece investigação",
    FindingStatus.UNABLE_TO_ASSESS: "Impossível avaliar com os dados disponíveis",
    FindingStatus.NOT_APPLICABLE: "Não aplicável ao escopo declarado (revisão humana necessária)",
}


def _verify_evidence_against_repo(
    evidences: List[EvidenceItem],
    repo_path: Path,
) -> List[EvidenceItem]:
    """Ensure no evidence points to a non-existent file or invalid line number in the repository."""
    validated: List[EvidenceItem] = []
    for ev in evidences:
        target = (repo_path / ev.file).resolve()
        if not target.exists() or not target.is_file():
            continue
        try:
            total_lines = max(1, len(target.read_bytes().splitlines()))
        except Exception:
            total_lines = 1
        l_start = min(max(1, ev.line_start or 1), total_lines)
        l_end = min(max(l_start, ev.line_end or l_start), total_lines)
        validated.append(
            ev.model_copy(update={"line_start": l_start, "line_end": l_end})
        )
    return validated


def _eval_r01(rule: RuleDefinition, analysis: Dict[str, Any], repo_path: Path) -> Finding:
    summary = analysis["inspection_summary"]
    total_py = summary["python_files_found"]
    success_py = summary["python_files_parsed_successfully"]
    failed_py = summary["python_files_failed"]
    coverage = summary["inspection_coverage_percent"]

    evidences: List[EvidenceItem] = []
    for f_ok in analysis["parsed_files"][:15]:
        evidences.append(
            EvidenceItem(
                file=f_ok["file"],
                symbol="<module>",
                line_start=1,
                line_end=f_ok["line_count"],
                evidence_type="parsed_python_file",
                description=f"Arquivo Python analisado com sucesso (SHA-256: {f_ok['sha256'][:12]}...)",
                metadata={"sha256": f_ok["sha256"], "line_count": f_ok["line_count"]},
            )
        )
    for f_err in analysis["failed_files"]:
        line_no = f_err.get("line") or 1
        evidences.append(
            EvidenceItem(
                file=f_err["file"],
                symbol="<parse_error>",
                line_start=line_no,
                line_end=line_no,
                evidence_type="ast_parse_failure",
                description=f"Falha no parsing AST ({f_err['error_type']}): {f_err['reason']}",
                metadata=f_err,
            )
        )

    evidences = _verify_evidence_against_repo(evidences, repo_path)

    if total_py == 0:
        status = FindingStatus.UNABLE_TO_ASSESS
        priority = ReviewPriority.HIGH
        desc = (
            "Impossível avaliar com os dados disponíveis: nenhum arquivo Python (.py) foi encontrado "
            f"entre os {summary['total_files_found']} arquivos inspecionados no repositório."
        )
        justification = "O escopo da versão V1.0 analisa exclusivamente arquivos Python (.py)."
        action = "Verificar se o caminho do repositório está correto ou se o software utiliza outra linguagem."
    elif failed_py == 0:
        status = FindingStatus.OBSERVED
        priority = ReviewPriority.INFORMATIONAL
        desc = (
            f"Evidência identificada: todos os {total_py} arquivos Python encontrados foram analisados "
            f"com sucesso via AST (cobertura de inspeção: {coverage}%)."
        )
        justification = f"Inspeção concluída sem falhas de parsing em {success_py}/{total_py} arquivos Python."
        action = "Manter a verificação sintática íntegra no fluxo de desenvolvimento."
    elif success_py > 0:
        status = FindingStatus.PARTIAL
        priority = ReviewPriority.HIGH
        failed_names = ", ".join(f["file"] for f in analysis["failed_files"])
        desc = (
            f"Evidência parcial: {success_py} de {total_py} arquivos Python foram analisados com sucesso "
            f"({coverage}%), mas {failed_py} arquivo(s) falharam no parsing AST ({failed_names})."
        )
        justification = (
            f"Arquivos com falha não puderam ter sua AST extraída ({failed_names}); "
            "nenhum arquivo com falha foi ignorado silenciosamente."
        )
        action = (
            "Corrigir os erros de sintaxe ou codificação nos arquivos listados e reexecutar a triagem "
            "para garantir cobertura completa."
        )
    else:
        status = FindingStatus.UNABLE_TO_ASSESS
        priority = ReviewPriority.HIGH
        desc = (
            f"Impossível avaliar com os dados disponíveis: todos os {total_py} arquivos Python encontrados "
            "falharam durante o parsing sintático AST."
        )
        justification = "Nenhum arquivo Python pôde ser convertido em AST devido a erros de sintaxe ou leitura."
        action = "Inspecionar e corrigir os erros de sintaxe/codificação antes de repetir a pré-auditoria."

    return Finding(
        finding_id="TA-001",
        rule_id=rule.rule_id,
        title=rule.title,
        category=rule.category,
        status=status,
        status_label_pt=STATUS_LABELS_PT[status],
        review_priority=priority,
        confidence=ConfidenceLevel.HIGH,
        description=desc,
        justification=justification,
        evidence=evidences,
        regulatory_references=[ref.model_copy() for ref in rule.normative_references],
        limitations=list(rule.limitations),
        recommended_action=action,
        human_review_required=True,
    )


def _eval_r02(rule: RuleDefinition, analysis: Dict[str, Any], repo_path: Path) -> Finding:
    deps = analysis["dependencies"]
    dep_files = deps["dependency_files"]
    declared = deps["declared_dependencies"]
    pinned_count = deps["pinned_count"]
    unpinned_count = deps["unpinned_count"]
    undeclared_imports = deps["undeclared_third_party_imports"]
    ai_comps = deps["ai_ml_components"]

    evidences: List[EvidenceItem] = []
    for d in declared[:25]:
        evidences.append(
            EvidenceItem(
                file=d["source_file"],
                symbol=d["package"],
                line_start=d["line"],
                line_end=d["line"],
                evidence_type="dependency_declaration",
                description=(
                    f"Pacote '{d['package']}' declarado em '{d['source_file']}' "
                    f"(especificador: '{d['version_spec'] or 'sem versão'}', fixado: {d['is_pinned']}, "
                    f"importado no código: {d['is_imported_in_code']})"
                ),
                metadata=d,
            )
        )

    if undeclared_imports:
        # Attach import evidence from parsed files
        for pf in analysis["parsed_files"]:
            for imp in undeclared_imports:
                if imp in pf["imports"]:
                    evidences.append(
                        EvidenceItem(
                            file=pf["file"],
                            symbol=imp,
                            line_start=1,
                            line_end=1,
                            evidence_type="undeclared_import",
                            description=(
                                f"Módulo externo '{imp}' importado em '{pf['file']}', "
                                "mas não localizado nos manifestos de dependências inspecionados."
                            ),
                        )
                    )

    evidences = _verify_evidence_against_repo(evidences, repo_path)

    if not dep_files:
        status = FindingStatus.NOT_OBSERVED
        priority = ReviewPriority.HIGH
        desc = (
            "Evidência não identificada no repositório analisado: não foram localizados arquivos "
            "de gerenciamento de dependências (requirements.txt, pyproject.toml, poetry.lock). "
            f"Foram identificados {len(undeclared_imports)} módulos externos importados no código "
            f"({', '.join(undeclared_imports[:10]) or 'nenhum'}). Possível lacuna documental de SOUP."
        )
        justification = "Ausência de manifesto de dependências observável no diretório inspecionado."
        action = (
            "Documentar todas as bibliotecas externas (SOUP) em manifesto versionado (ex.: requirements.txt "
            "ou pyproject.toml) e elaborar a lista formal de SOUP conforme IEC 62304 (Seção 8.1.2 e 5.3.3)."
        )
    elif declared and unpinned_count == 0 and not undeclared_imports:
        status = FindingStatus.OBSERVED
        priority = ReviewPriority.LOW
        desc = (
            f"Evidência identificada: arquivo(s) de dependências ({', '.join(dep_files)}) presentes com "
            f"{pinned_count} dependência(s) com versão exata fixada (==). "
            f"Componentes de IA/ML identificados: {', '.join(ai_comps) or 'nenhum'}."
        )
        justification = "Todas as dependências declaradas possuem versão fixada e cobrem os imports observados."
        action = (
            "Revisão humana necessária para verificar se cada item de SOUP possui requisitos funcionais, "
            "avaliação de risco e verificação de lista de anomalias documentados no dossiê técnico."
        )
    else:
        status = FindingStatus.PARTIAL
        priority = ReviewPriority.MEDIUM
        desc = (
            f"Evidência parcial: manifesto(s) de dependências localizado(s) ({', '.join(dep_files)}), "
            f"contendo {pinned_count} pacote(s) com versão fixada e {unpinned_count} pacote(s) sem versão "
            f"exata fixada. Imports externos não declarados no manifesto: "
            f"{', '.join(undeclared_imports) or 'nenhum'}. "
            f"Componentes de IA/ML: {', '.join(ai_comps) or 'nenhum'}."
        )
        justification = (
            "A presença de dependências sem versão fixada ou imports omitidos não representa automaticamente "
            "uma não conformidade, mas é um indicador técnico que merece investigação para controle de SOUP."
        )
        action = (
            "Avaliar o congelamento de versões (pinning/lockfile), reconciliar bibliotecas importadas no código "
            "com o manifesto e manter a matriz de rastreabilidade de SOUP atualizada."
        )

    return Finding(
        finding_id="TA-002",
        rule_id=rule.rule_id,
        title=rule.title,
        category=rule.category,
        status=status,
        status_label_pt=STATUS_LABELS_PT[status],
        review_priority=priority,
        confidence=ConfidenceLevel.HIGH,
        description=desc,
        justification=justification,
        evidence=evidences,
        regulatory_references=[ref.model_copy() for ref in rule.normative_references],
        limitations=list(rule.limitations),
        recommended_action=action,
        human_review_required=True,
    )


def _eval_r03(rule: RuleDefinition, analysis: Dict[str, Any], repo_path: Path) -> Finding:
    tci = analysis["tests_and_ci"]
    test_dirs = tci["test_directories"]
    test_files = tci["test_files"]
    frameworks = tci["test_frameworks"]
    configs = tci["test_configs"]

    evidences: List[EvidenceItem] = []
    for tf in test_files:
        pf_match = next((p for p in analysis["parsed_files"] if p["file"] == tf), None)
        funcs = pf_match["functions"] if pf_match else []
        test_funcs = [fn for fn in funcs if fn["name"].startswith("test_") or fn["is_method"]]
        evidences.append(
            EvidenceItem(
                file=tf,
                symbol=test_funcs[0]["symbol"] if test_funcs else "<test_module>",
                line_start=test_funcs[0]["line_start"] if test_funcs else 1,
                line_end=test_funcs[0]["line_end"] if test_funcs else 1,
                evidence_type="test_module",
                description=(
                    f"Módulo de teste '{tf}' identificado "
                    f"({len(test_funcs)} funções/métodos candidatos de teste)."
                ),
                metadata={"test_functions": [f["symbol"] for f in test_funcs]},
            )
        )

    for cfg in configs:
        evidences.append(
            EvidenceItem(
                file=cfg,
                symbol="<test_config>",
                line_start=1,
                line_end=1,
                evidence_type="test_configuration",
                description=f"Arquivo de configuração de testes '{cfg}' identificado.",
            )
        )

    evidences = _verify_evidence_against_repo(evidences, repo_path)

    total_test_funcs = sum(len(ev.metadata.get("test_functions", [])) for ev in evidences if ev.evidence_type == "test_module")

    if test_files and total_test_funcs > 0:
        status = FindingStatus.OBSERVED
        priority = ReviewPriority.LOW
        desc = (
            f"Evidência identificada: {len(test_files)} arquivo(s) de teste localizado(s) "
            f"(diretórios: {', '.join(test_dirs) or 'raiz/módulos'}; frameworks: "
            f"{', '.join(frameworks) or 'não identificado explicitamente'}; "
            f"{total_test_funcs} função(ões)/método(s) de teste)."
        )
        justification = "Módulos e funções de teste automatizado foram observados no repositório."
        action = (
            "Revisão humana necessária para verificar a rastreabilidade entre os casos de teste automatizados, "
            "os requisitos de software e os controles de risco (IEC 62304 Seções 5.5, 5.6 e 5.7)."
        )
    elif test_files or test_dirs or configs:
        status = FindingStatus.PARTIAL
        priority = ReviewPriority.MEDIUM
        desc = (
            f"Evidência parcial: estrutura ou configuração de testes presente "
            f"(diretórios: {', '.join(test_dirs) or 'nenhum'}, arquivos: {len(test_files)}, "
            f"configs: {', '.join(configs) or 'nenhuma'}), mas sem funções de teste verificáveis."
        )
        justification = "Estrutura parcial de testes localizada sem casos de teste completos observáveis via AST."
        action = "Implementar e vincular os testes de unidade, integração e sistema aos requisitos do software."
    else:
        status = FindingStatus.NOT_OBSERVED
        priority = ReviewPriority.HIGH
        desc = (
            "Evidência não identificada no repositório analisado: não foram localizados diretórios de teste "
            "(tests/, test/) nem arquivos de teste (test_*.py, *_test.py). "
            "A ausência no repositório é relatada como ausência de evidência observável, "
            "e não como prova de que a organização não executa testes."
        )
        justification = "Nenhum arquivo ou diretório de testes automatizados encontrado no escopo inspecionado."
        action = (
            "Investigar onde os artefatos de verificação de unidades e testes de sistema estão mantidos "
            "e incorporar suíte de testes automatizados reproduzível ao controle de versão."
        )

    return Finding(
        finding_id="TA-003",
        rule_id=rule.rule_id,
        title=rule.title,
        category=rule.category,
        status=status,
        status_label_pt=STATUS_LABELS_PT[status],
        review_priority=priority,
        confidence=ConfidenceLevel.HIGH,
        description=desc,
        justification=justification,
        evidence=evidences,
        regulatory_references=[ref.model_copy() for ref in rule.normative_references],
        limitations=list(rule.limitations),
        recommended_action=action,
        human_review_required=True,
    )


def _eval_r04(rule: RuleDefinition, analysis: Dict[str, Any], repo_path: Path) -> Finding:
    tci = analysis["tests_and_ci"]
    workflows = tci["ci_workflows"]
    cov_evidences = tci["coverage_evidences"]

    evidences: List[EvidenceItem] = []
    for wf in workflows:
        evidences.append(
            EvidenceItem(
                file=wf["file"],
                symbol="ci_workflow",
                line_start=1,
                line_end=1,
                evidence_type="ci_workflow",
                description=(
                    f"Workflow CI '{wf['file']}' (comandos de teste: "
                    f"{', '.join(wf['test_commands']) or 'nenhum detectado'}; "
                    f"cobertura: {wf['has_coverage']})"
                ),
                metadata=wf,
            )
        )

    evidences = _verify_evidence_against_repo(evidences, repo_path)
    has_test_cmds = any(len(wf["test_commands"]) > 0 for wf in workflows)

    if workflows and has_test_cmds:
        status = FindingStatus.OBSERVED
        priority = ReviewPriority.LOW
        desc = (
            f"Evidência identificada: {len(workflows)} configuração(ões) de CI/CD localizada(s) "
            f"com comandos declarados para execução automatizada de testes "
            f"(evidências de cobertura: {', '.join(cov_evidences) or 'não identificadas'})."
        )
        justification = "Arquivos de workflow CI/CD contendo etapas de execução de testes foram encontrados."
        action = (
            "Verificar se os registros de execução do CI/CD são arquivados como evidência de verificação "
            "e regressão a cada versão liberada (IEC 62304 Seção 5.6.6 e 5.8)."
        )
    elif workflows:
        status = FindingStatus.PARTIAL
        priority = ReviewPriority.MEDIUM
        desc = (
            f"Evidência parcial: arquivo(s) de workflow CI/CD encontrado(s) "
            f"({', '.join(w['file'] for w in workflows)}), porém sem comandos explícitos "
            "de execução de testes Python (pytest/unittest) identificados."
        )
        justification = "Configuração de CI presente, mas sem etapa observável de teste automatizado."
        action = "Incluir etapa de execução de testes automatizados e verificação no pipeline de CI/CD."
    else:
        status = FindingStatus.NOT_OBSERVED
        priority = ReviewPriority.MEDIUM
        desc = (
            "Evidência não identificada no repositório analisado: nenhuma configuração de CI/CD "
            "(.github/workflows/*.yml ou .gitlab-ci.yml) foi encontrada no escopo inspecionado."
        )
        justification = "Ausência de arquivos de configuração de integração contínua no repositório."
        action = (
            "Avaliar a adoção de pipeline de CI/CD versionado para automatizar testes de regressão "
            "ou documentar o ambiente externo utilizado para verificação."
        )

    return Finding(
        finding_id="TA-004",
        rule_id=rule.rule_id,
        title=rule.title,
        category=rule.category,
        status=status,
        status_label_pt=STATUS_LABELS_PT[status],
        review_priority=priority,
        confidence=ConfidenceLevel.HIGH,
        description=desc,
        justification=justification,
        evidence=evidences,
        regulatory_references=[ref.model_copy() for ref in rule.normative_references],
        limitations=list(rule.limitations),
        recommended_action=action,
        human_review_required=True,
    )


def _eval_r05(rule: RuleDefinition, analysis: Dict[str, Any], repo_path: Path) -> Finding:
    io_ops: List[Dict[str, Any]] = []
    try_blocks: List[Dict[str, Any]] = []
    evidences: List[EvidenceItem] = []

    for pf in analysis["parsed_files"]:
        fname = pf["file"]
        for io_item in pf["io_operations"]:
            entry = {**io_item, "file": fname}
            io_ops.append(entry)
            evidences.append(
                EvidenceItem(
                    file=fname,
                    symbol=io_item["symbol"],
                    line_start=io_item["line_start"],
                    line_end=io_item["line_end"],
                    evidence_type="ast_io_operation",
                    description=(
                        f"Operação candidata de I/O '{io_item['call']}' em '{io_item['symbol'] or '<module>'}' "
                        f"(dentro de try-except não vazio: {io_item['inside_non_empty_try']})"
                    ),
                    metadata=entry,
                )
            )
        for tb in pf["try_blocks"]:
            tb_entry = {**tb, "file": fname}
            try_blocks.append(tb_entry)
            if tb["has_empty_except"] or tb["has_pass_in_except"]:
                evidences.append(
                    EvidenceItem(
                        file=fname,
                        symbol=tb["symbol"],
                        line_start=tb["line_start"],
                        line_end=tb["line_end"],
                        evidence_type="ast_empty_or_pass_except",
                        description=(
                            f"Bloco try-except em '{tb['symbol'] or '<module>'}' possui handler vazio "
                            f"ou com instrução 'pass' (exceções: {', '.join(tb['exception_types'])})"
                        ),
                        metadata=tb_entry,
                    )
                )

    evidences = _verify_evidence_against_repo(evidences, repo_path)

    total_io = len(io_ops)
    protected_io = sum(1 for op in io_ops if op["inside_non_empty_try"])
    unprotected_io = total_io - protected_io
    empty_or_pass_Count = sum(
        1 for tb in try_blocks if tb["has_empty_except"] or tb["has_pass_in_except"]
    )

    if total_io == 0 and len(try_blocks) == 0:
        status = FindingStatus.NOT_OBSERVED
        priority = ReviewPriority.LOW
        desc = (
            "Evidência não identificada no repositório analisado: não foram detectadas chamadas "
            "candidatas de I/O nem blocos try-except nos arquivos Python inspecionados."
        )
        justification = "Nenhuma operação candidata de leitura/escrita ou bloco de exceção localizado."
        action = "Verificar se a ingestão de dados ocorre em módulos externos e revisar o controle de falhas."
    elif total_io > 0 and unprotected_io == 0 and empty_or_pass_Count == 0:
        status = FindingStatus.OBSERVED
        priority = ReviewPriority.MEDIUM
        desc = (
            f"Evidência identificada: todas as {total_io} operação(ões) candidatas de I/O detectadas "
            "estão inseridas em blocos try-except não vazios, sem blocos except silenciosos (pass)."
        )
        justification = (
            f"{protected_io}/{total_io} chamadas de I/O possuem estrutura sintática try-except local. "
            "A presença sintática não comprova adequação do controle de risco."
        )
        action = (
            "Revisão humana necessária para confirmar se as exceções capturadas produzem mensagens de erro "
            "seguras, logs auditáveis e estado seguro para o paciente/usuário."
        )
    elif protected_io > 0 or (len(try_blocks) > 0 and empty_or_pass_Count < len(try_blocks)):
        status = FindingStatus.PARTIAL
        priority = ReviewPriority.HIGH
        desc = (
            f"Evidência parcial: entre {total_io} operação(ões) candidatas de I/O, {protected_io} possuem "
            f"bloco try-except não vazio e {unprotected_io} não possuem tratamento local observável. "
            f"Foram identificados {empty_or_pass_Count} bloco(s) except vazios ou com 'pass'."
        )
        justification = (
            "Indicador técnico que merece investigação: coexistem operações de I/O sem captura local de "
            "exceção ou blocos except que suprimem falhas com pass."
        )
        action = (
            "Revisar cada operação de leitura/escrita sem tratamento de erro e eliminar blocos except "
            "vazios/pass que possam mascarar corrupção de arquivos ou dados clínicos."
        )
    else:
        status = FindingStatus.NOT_OBSERVED
        priority = ReviewPriority.HIGH
        desc = (
            f"Evidência não identificada no repositório analisado: foram detectadas {total_io} operação(ões) "
            "candidatas de I/O sem nenhum bloco try-except não vazio associado "
            f"(blocos except vazios/pass encontrados: {empty_or_pass_Count})."
        )
        justification = (
            "Operações de leitura/escrita identificadas sem tratamento de exceções efetivo observável no escopo local."
        )
        action = (
            "Implementar tratamento estruturado de exceções para operações de leitura/escrita de dados e "
            "artefatos, vinculando o tratamento à análise de riscos do software."
        )

    return Finding(
        finding_id="TA-005",
        rule_id=rule.rule_id,
        title=rule.title,
        category=rule.category,
        status=status,
        status_label_pt=STATUS_LABELS_PT[status],
        review_priority=priority,
        confidence=ConfidenceLevel.HIGH,
        description=desc,
        justification=justification,
        evidence=evidences[:30],
        regulatory_references=[ref.model_copy() for ref in rule.normative_references],
        limitations=list(rule.limitations),
        recommended_action=action,
        human_review_required=True,
    )


def _eval_r06(rule: RuleDefinition, analysis: Dict[str, Any], repo_path: Path) -> Finding:
    val_signals: List[Dict[str, Any]] = []
    evidences: List[EvidenceItem] = []

    for pf in analysis["parsed_files"]:
        fname = pf["file"]
        for vs in pf["validation_signals"]:
            entry = {**vs, "file": fname}
            val_signals.append(entry)
            evidences.append(
                EvidenceItem(
                    file=fname,
                    symbol=vs.get("symbol"),
                    line_start=vs["line_start"],
                    line_end=vs["line_end"],
                    evidence_type=f"validation_{vs['signal_type']}",
                    description=(
                        f"Sinal de validação ({vs['signal_type']}) em '{vs.get('symbol') or '<module>'}'"
                    ),
                    metadata=entry,
                )
            )

    evidences = _verify_evidence_against_repo(evidences, repo_path)

    dedicated_funcs = [
        v for v in val_signals if v["signal_type"] in {"validation_function_definition", "validation_call"}
    ]
    raising_guards = [
        v for v in val_signals if v["signal_type"] == "conditional_guard" and v.get("raises_exception")
    ]

    if dedicated_funcs or raising_guards:
        status = FindingStatus.OBSERVED
        priority = ReviewPriority.MEDIUM
        desc = (
            f"Evidência identificada: {len(val_signals)} sinal(is) estrutural(is) de validação de entrada "
            f"localizado(s), incluindo {len(dedicated_funcs)} função(ões)/chamada(s) de validação e "
            f"{len(raising_guards)} guarda(s) condicional(is) com levantamento de exceção."
        )
        justification = (
            "Foram identificados mecanismos explícitos de verificação de entrada no código. "
            "A presença estrutural não garante suficiência clínica ou completude da validação."
        )
        action = (
            "Revisão humana necessária para verificar se os critérios de validação cobrem formatos inválidos, "
            "valores ausentes, limites fisiológicos/dimensionais e proteção contra entradas malformadas."
        )
    elif val_signals:
        status = FindingStatus.PARTIAL
        priority = ReviewPriority.MEDIUM
        desc = (
            f"Evidência parcial: foram identificados {len(val_signals)} sinal(is) genérico(s) de verificação "
            "(como instruções assert ou checagens condicionais simples sem levantamento explícito de erro)."
        )
        justification = (
            "Apenas verificações simples ou asserts foram detectados; asserts podem ser ignorados em tempo de execução."
        )
        action = (
            "Substituir verificações baseadas apenas em assert por rotinas explícitas de validação de entradas "
            "nas fronteiras de ingestão de dados e antes da inferência."
        )
    else:
        status = FindingStatus.NOT_OBSERVED
        priority = ReviewPriority.HIGH
        desc = (
            "Evidência não identificada no repositório analisado: não foram detectadas funções dedicadas "
            "de validação de entrada, chamadas de validação de schema nem guardas condicionais explícitas."
        )
        justification = "Ausência de sinais estruturais observáveis de validação de dados de entrada na AST."
        action = (
            "Implementar validação explícita de tipos, dimensões, intervalos e integridade dos dados de "
            "entrada antes do processamento clínico ou execução de modelos."
        )

    return Finding(
        finding_id="TA-006",
        rule_id=rule.rule_id,
        title=rule.title,
        category=rule.category,
        status=status,
        status_label_pt=STATUS_LABELS_PT[status],
        review_priority=priority,
        confidence=ConfidenceLevel.MEDIUM,
        description=desc,
        justification=justification,
        evidence=evidences[:30],
        regulatory_references=[ref.model_copy() for ref in rule.normative_references],
        limitations=list(rule.limitations),
        recommended_action=action,
        human_review_required=True,
    )


def _eval_r07(
    rule: RuleDefinition,
    analysis: Dict[str, Any],
    profile: ProductProfile,
    repo_path: Path,
) -> Finding:
    artifacts: List[Dict[str, Any]] = []
    evidences: List[EvidenceItem] = []

    for pf in analysis["parsed_files"]:
        fname = pf["file"]
        for ma in pf["model_artifacts"]:
            entry = {**ma, "file": fname}
            artifacts.append(entry)
            evidences.append(
                EvidenceItem(
                    file=fname,
                    symbol=ma.get("symbol"),
                    line_start=ma["line_start"],
                    line_end=ma["line_end"],
                    evidence_type=f"model_{ma['action']}",
                    description=(
                        f"Operação/referência de modelo ({ma['action']}) em '{ma.get('symbol') or '<module>'}'"
                    ),
                    metadata=entry,
                )
            )

    for mf in analysis["standalone_model_files"]:
        evidences.append(
            EvidenceItem(
                file=mf,
                symbol=Path(mf).name,
                line_start=1,
                line_end=1,
                evidence_type="standalone_model_file",
                description=f"Arquivo binário/checkpoint de modelo localizado no repositório: '{mf}'",
            )
        )

    evidences = _verify_evidence_against_repo(evidences, repo_path)
    ai_comps = analysis["dependencies"]["ai_ml_components"]
    has_any_ai_signal = bool(
        ai_comps
        or artifacts
        or analysis["standalone_model_files"]
        or any(pf["training_signals"] or pf["inference_signals"] for pf in analysis["parsed_files"])
    )

    if profile.ai_components is False and not has_any_ai_signal:
        status = FindingStatus.NOT_APPLICABLE
        priority = ReviewPriority.INFORMATIONAL
        desc = (
            "Não aplicável: o perfil do produto declara ausência de componentes de IA (ai_components=false) "
            "e nenhum framework ou artefato de aprendizado de máquina foi identificado no repositório."
        )
        justification = (
            "Regra R07 específica para artefatos de modelos de IA/ML; inaplicável quando o software não "
            "utiliza modelos de aprendizado de máquina segundo o perfil e a inspeção estática."
        )
        action = "Nenhuma ação necessária para modelos de ML, desde que confirmado que o produto não incorpora IA."
    elif evidences:
        status = FindingStatus.PARTIAL
        priority = ReviewPriority.HIGH
        desc = (
            f"Evidência parcial: foram identificados {len(evidences)} sinal(is) de carregamento, salvamento "
            f"ou referência a checkpoints de modelos ({len(analysis['standalone_model_files'])} arquivo(s) "
            "de modelo no repositório). A existência de chamadas de carga ou arquivos .pt/.pth/.onnx "
            "não comprova proveniência completa nem controle de versão do modelo."
        )
        justification = (
            "Indicador técnico que merece investigação: artefatos de modelo exigem rastreabilidade documental "
            "de versão, dataset de treinamento, hiperparâmetros e verificação de integridade (hash)."
        )
        action = (
            "Documentar formalmente a proveniência de cada modelo carregado (identificador de versão, hash SHA-256 "
            "do artefato, dataset de origem, hiperparâmetros e Relatório de Validação de Algoritmo)."
        )
    else:
        status = FindingStatus.NOT_OBSERVED
        priority = ReviewPriority.MEDIUM
        desc = (
            "Evidência não identificada no repositório analisado: não foram localizadas chamadas explícitas "
            "de carregamento/salvamento de artefatos de modelos nem arquivos de checkpoint no escopo inspecionado."
        )
        justification = (
            "Nenhum ponto observável de persistência ou carregamento de pesos de modelo foi encontrado na AST."
        )
        action = (
            "Caso o software utilize modelos de IA/ML, identificar onde os artefatos de modelo são armazenados, "
            "carregados e versionados."
        )

    return Finding(
        finding_id="TA-007",
        rule_id=rule.rule_id,
        title=rule.title,
        category=rule.category,
        status=status,
        status_label_pt=STATUS_LABELS_PT[status],
        review_priority=priority,
        confidence=ConfidenceLevel.HIGH,
        description=desc,
        justification=justification,
        evidence=evidences[:30],
        regulatory_references=[ref.model_copy() for ref in rule.normative_references],
        limitations=list(rule.limitations),
        recommended_action=action,
        human_review_required=True,
    )


def _eval_r08(
    rule: RuleDefinition,
    analysis: Dict[str, Any],
    profile: ProductProfile,
    repo_path: Path,
) -> Finding:
    train_files: Dict[str, List[Dict[str, Any]]] = {}
    infer_files: Dict[str, List[Dict[str, Any]]] = {}
    evidences: List[EvidenceItem] = []

    for pf in analysis["parsed_files"]:
        fname = pf["file"]
        if pf["training_signals"]:
            train_files[fname] = pf["training_signals"]
            for ts in pf["training_signals"]:
                evidences.append(
                    EvidenceItem(
                        file=fname,
                        symbol=ts.get("symbol"),
                        line_start=ts["line_start"],
                        line_end=ts["line_end"],
                        evidence_type="ast_training_signal",
                        description=(
                            f"Sinal estrutural de treinamento ({ts['signal_type']}) em "
                            f"'{ts.get('symbol') or '<module>'}'"
                        ),
                        metadata=ts,
                    )
                )
        if pf["inference_signals"]:
            infer_files[fname] = pf["inference_signals"]
            for inf in pf["inference_signals"]:
                evidences.append(
                    EvidenceItem(
                        file=fname,
                        symbol=inf.get("symbol"),
                        line_start=inf["line_start"],
                        line_end=inf["line_end"],
                        evidence_type="ast_inference_signal",
                        description=(
                            f"Sinal estrutural de inferência ({inf['signal_type']}) em "
                            f"'{inf.get('symbol') or '<module>'}'"
                        ),
                        metadata=inf,
                    )
                )

    evidences = _verify_evidence_against_repo(evidences, repo_path)
    ai_comps = analysis["dependencies"]["ai_ml_components"]
    has_any_ai = bool(ai_comps or train_files or infer_files or analysis["standalone_model_files"])

    overlapping_files = sorted(set(train_files.keys()) & set(infer_files.keys()))

    if profile.ai_components is False and not has_any_ai:
        status = FindingStatus.NOT_APPLICABLE
        priority = ReviewPriority.INFORMATIONAL
        desc = (
            "Não aplicável: o perfil do software indica ausência de componentes de IA (ai_components=false) "
            "e não foram encontrados sinais estruturais de treinamento ou inferência."
        )
        justification = "Regra R08 aplicável apenas a sistemas que possuem rotinas de aprendizado de máquina."
        action = "Confirmar que o escopo do produto não inclui algoritmos treináveis."
    elif train_files and infer_files and not overlapping_files:
        status = FindingStatus.OBSERVED
        priority = ReviewPriority.LOW
        desc = (
            f"Evidência identificada: sinais estruturais de treinamento ({len(train_files)} arquivo(s): "
            f"{', '.join(train_files.keys())}) e de inferência ({len(infer_files)} arquivo(s): "
            f"{', '.join(infer_files.keys())}) encontram-se distribuídos em módulos distintos."
        )
        justification = (
            "Não foi observado acoplamento no mesmo arquivo entre sinais de treinamento e inferência. "
            "Isso não prova isolamento de ambiente em produção sem análise do fluxo de execução."
        )
        action = (
            "Revisão humana necessária para confirmar que o pacote de implantação em produção não executa "
            "rotinas de treinamento ou atualização não controlada de pesos."
        )
    elif overlapping_files:
        status = FindingStatus.PARTIAL
        priority = ReviewPriority.HIGH
        desc = (
            f"Evidência parcial: sinais estruturais de treinamento e de inferência coexistem no(s) mesmo(s) "
            f"arquivo(s) ({', '.join(overlapping_files)}). Indicador técnico que merece investigação "
            "quanto à segregação arquitetural entre desenvolvimento/treino e produção/inferência."
        )
        justification = (
            f"Coexistência de sinais de treinamento e inferência em {', '.join(overlapping_files)}. "
            "Requer inspeção humana do fluxo de controle para verificar se o modelo é congelado em produção."
        )
        action = (
            "Revisar a arquitetura dos módulos listados para separar claramente os scripts de treinamento "
            "do pipeline de inferência clínica e documentar o controle de implantação (SOP Deployment)."
        )
    elif train_files or infer_files:
        status = FindingStatus.PARTIAL
        priority = ReviewPriority.MEDIUM
        which_found = "apenas sinais de treinamento" if train_files else "apenas sinais de inferência"
        desc = (
            f"Evidência parcial: foram identificados {which_found} no repositório analisado "
            f"(arquivos de treino: {len(train_files)}; arquivos de inferência: {len(infer_files)})."
        )
        justification = (
            "Apenas uma das etapas do ciclo de vida do modelo está visível estruturalmente neste repositório."
        )
        action = (
            "Verificar se a outra etapa (treinamento ou inferência em produção) reside em repositório separado "
            "e documentar a interface e transferência controlada dos artefatos de modelo."
        )
    else:
        status = FindingStatus.NOT_OBSERVED
        priority = ReviewPriority.MEDIUM
        desc = (
            "Evidência não identificada no repositório analisado: não foram detectados sinais estruturais "
            "explícitos de rotinas de treinamento nem de inferência nos arquivos Python inspecionados."
        )
        justification = "Nenhuma função ou chamada típica de treinamento/inferência foi localizada pela AST."
        action = "Revisar manualmente os pontos de entrada do algoritmo e a arquitetura do software."

    return Finding(
        finding_id="TA-008",
        rule_id=rule.rule_id,
        title=rule.title,
        category=rule.category,
        status=status,
        status_label_pt=STATUS_LABELS_PT[status],
        review_priority=priority,
        confidence=ConfidenceLevel.MEDIUM,
        description=desc,
        justification=justification,
        evidence=evidences[:30],
        regulatory_references=[ref.model_copy() for ref in rule.normative_references],
        limitations=list(rule.limitations),
        recommended_action=action,
        human_review_required=True,
    )


def evaluate_all_rules(
    analysis: Dict[str, Any],
    profile: ProductProfile,
    repo_path: Optional[Path] = None,
) -> List[Finding]:
    """Run all 8 deterministic rules (R01-R08) and return validated Finding models."""
    resolved_repo = Path(repo_path or analysis["repository_path"]).resolve()
    catalog = get_rule_catalog_dict()

    findings: List[Finding] = [
        _eval_r01(catalog["R01"], analysis, resolved_repo),
        _eval_r02(catalog["R02"], analysis, resolved_repo),
        _eval_r03(catalog["R03"], analysis, resolved_repo),
        _eval_r04(catalog["R04"], analysis, resolved_repo),
        _eval_r05(catalog["R05"], analysis, resolved_repo),
        _eval_r06(catalog["R06"], analysis, resolved_repo),
        _eval_r07(catalog["R07"], analysis, profile, resolved_repo),
        _eval_r08(catalog["R08"], analysis, profile, resolved_repo),
    ]
    return findings

