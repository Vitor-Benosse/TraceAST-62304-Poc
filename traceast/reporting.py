"""Report and manifest generator for TraceAST-62304 (JSON and Markdown outputs)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from traceast import __positioning__, __tool_name__, __version__
from traceast.config import MANDATORY_DISCLAIMERS
from traceast.models import (
    Finding,
    FindingStatus,
    FindingsReport,
    ProductProfile,
    ReviewPriority,
)


def compute_summary_counts(findings: List[Finding]) -> Dict[str, int]:
    return {
        "total_findings": len(findings),
        "observed": sum(1 for f in findings if f.status == FindingStatus.OBSERVED),
        "partial": sum(1 for f in findings if f.status == FindingStatus.PARTIAL),
        "not_observed": sum(1 for f in findings if f.status == FindingStatus.NOT_OBSERVED),
        "unable_to_assess": sum(1 for f in findings if f.status == FindingStatus.UNABLE_TO_ASSESS),
        "not_applicable": sum(1 for f in findings if f.status == FindingStatus.NOT_APPLICABLE),
        "human_review_required": sum(1 for f in findings if f.human_review_required),
    }


def render_markdown_report(
    report: FindingsReport,
    analysis: Dict[str, Any],
    run_manifest: Dict[str, Any],
    retrieval_trace: Optional[Dict[str, Any]] = None,
) -> str:
    """Render the complete, structured Markdown pre-audit screening report (Sections A through F)."""
    lines: List[str] = []
    profile: ProductProfile = report.product_profile
    summary = analysis["inspection_summary"]
    counts = report.summary_counts

    lines.append(f"# Relatório de Triagem Pré-Auditoria — {__tool_name__} v{__version__}")
    lines.append("")
    lines.append(f"> **Posicionamento:** *{__positioning__}*")
    lines.append("")
    lines.append("### Avisos Regulatórios e Limitações Obrigatórias")
    for disc in report.mandatory_disclaimers:
        lines.append(f"- {disc}")
    lines.append("")

    # Section A. Identificação
    lines.append("## A. Identificação")
    lines.append("")
    lines.append(f"- **Nome do Projeto:** {report.project_name}")
    lines.append(f"- **Commit SHA Analisado:** `{report.commit_sha or 'N/A (repositório sem commit Git identificável)'}`")
    lines.append(f"- **Data e Horário da Execução (UTC):** `{report.execution_timestamp}`")
    lines.append(f"- **Versão do {__tool_name__}:** `{report.tool_version}`")
    lines.append(f"- **Hash do Catálogo de Regras:** `{run_manifest.get('rule_catalog_sha256', 'N/A')}`")
    lines.append(f"- **Versão do Python:** `{analysis['python_version']}`")
    lines.append("")
    lines.append("### Perfil do Produto Informado pelo Usuário")
    lines.append(f"- **Nome declarado:** {profile.name}")
    lines.append(f"- **Finalidade médica pretendida (`intended_purpose`):** {profile.intended_purpose}")
    lines.append(f"- **Usuários pretendidos (`intended_users`):** {profile.intended_users}")
    lines.append(f"- **Mercado-alvo (`target_market`):** {', '.join(profile.target_market)}")
    lines.append(f"- **Tipo de software (`software_type`):** {profile.software_type}")
    lines.append(f"- **Componentes de IA declarados (`ai_components`):** `{profile.ai_components}`")
    lines.append(f"- **Contexto de decisão clínica (`clinical_decision_context`):** {profile.clinical_decision_context}")
    if profile.profile_limitations:
        lines.append("- **Limitações decorrentes do perfil:**")
        for plim in profile.profile_limitations:
            lines.append(f"  - {plim}")
    lines.append("")

    # Section B. Integridade da análise
    lines.append("## B. Integridade da Análise")
    lines.append("")
    lines.append(f"- **Quantidade total de arquivos encontrados:** {summary['total_files_found']}")
    lines.append(f"- **Quantidade de arquivos Python (`.py`):** {summary['python_files_found']}")
    lines.append(f"- **Arquivos Python analisados com sucesso:** {summary['python_files_parsed_successfully']}")
    lines.append(f"- **Arquivos Python que falharam na análise:** {summary['python_files_failed']}")
    lines.append(f"- **Percentual de cobertura da inspeção sintática:** {summary['inspection_coverage_percent']}%")
    lines.append("")
    if analysis["failed_files"]:
        lines.append("### Registro de Arquivos com Falha de Parsing")
        lines.append("| Arquivo | Tipo de Erro | Linha | Motivo Registrado |")
        lines.append("|---|---|---|---|")
        for ff in analysis["failed_files"]:
            lines.append(
                f"| `{ff['file']}` | `{ff['error_type']}` | {ff.get('line') or 'N/A'} | {ff['reason']} |"
            )
        lines.append("")
    else:
        lines.append("*Nenhum arquivo Python falhou durante o parsing sintático AST.*")
        lines.append("")

    # Section C. Visão geral
    lines.append("## C. Visão Geral dos Indicadores Técnicos")
    lines.append("")
    lines.append("| Estado do Indicador | Expressão Padronizada | Quantidade |")
    lines.append("|---|---|---|")
    lines.append(f"| `observed` | Evidência identificada | {counts['observed']} |")
    lines.append(f"| `partial` | Evidência parcial — indicador técnico que merece investigação | {counts['partial']} |")
    lines.append(f"| `not_observed` | Evidência não identificada no repositório analisado | {counts['not_observed']} |")
    lines.append(f"| `unable_to_assess` | Impossível avaliar com os dados disponíveis | {counts['unable_to_assess']} |")
    lines.append(f"| `not_applicable` | Não aplicável ao escopo declarado | {counts['not_applicable']} |")
    lines.append(f"| **Revisão Humana** | **Itens que exigem revisão humana (`human_review_required`)** | **{counts['human_review_required']}** |")
    lines.append("")

    # Section D. Achados detalhados
    lines.append("## D. Achados Detalhados")
    lines.append("")
    for f in report.findings:
        lines.append(f"### {f.finding_id} ({f.rule_id}) — {f.title}")
        lines.append(f"- **Categoria:** {f.category}")
        lines.append(f"- **Status:** `{f.status.value}` ({f.status_label_pt})")
        lines.append(f"- **Prioridade de Revisão Técnica:** `{f.review_priority.value}` *(Não representa classe de risco regulatório ou clínico)*")
        lines.append(f"- **Confiança da Detecção Sintática:** `{f.confidence.value}`")
        lines.append(f"- **Necessidade de Validação Humana:** `{'Sim' if f.human_review_required else 'Não'}`")
        lines.append(f"- **Descrição:** {f.description}")
        lines.append(f"- **Justificativa de Rastreabilidade:** {f.justification}")
        lines.append("")

        lines.append("#### Evidências Extraídas (Arquivos e Linhas)")
        if f.evidence:
            lines.append("| Arquivo | Símbolo | Linhas | Tipo | Descrição |")
            lines.append("|---|---|---|---|---|")
            for ev in f.evidence[:15]:
                sym = f"`{ev.symbol}`" if ev.symbol else "N/A"
                lines.append(
                    f"| `{ev.file}` | {sym} | {ev.line_start}–{ev.line_end} | `{ev.evidence_type}` | {ev.description} |"
                )
            if len(f.evidence) > 15:
                lines.append(f"*... e mais {len(f.evidence) - 15} evidência(s) registrada(s) em `findings.json`.*")
        else:
            lines.append("*Nenhuma evidência positiva localizada no código; ver justificativa acima.*")
        lines.append("")

        lines.append("#### Referências Regulatórias Relacionadas")
        for ref in f.regulatory_references:
            chunk_str = f" | Fragmento: `{ref.chunk_id}` (Score: `{ref.similarity_score}`)" if ref.chunk_id else ""
            lines.append(
                f"- **{ref.document_id}** ({ref.issuing_body}) — Cláusula/Seção: `{ref.clause or 'N/A'}` "
                f"| Status da Validação: `{ref.mapping_status.value}`{chunk_str}"
            )
        lines.append("")

        lines.append("#### Limitações Técnicas")
        for lim in f.limitations:
            lines.append(f"- {lim}")
        lines.append("")

        lines.append(f"#### Recomendação de Investigação ou Correção\n{f.recommended_action}")
        lines.append("")

        if f.llm_explanation is not None:
            lines.append("#### Explicação Complementar Assistida por IA (LLM Opcional)")
            lines.append(f"- **Explicação:** {f.llm_explanation.accessible_explanation}")
            if f.llm_explanation.suggested_documents_to_review:
                lines.append(
                    "- **Documentos sugeridos para revisão:** "
                    + ", ".join(f.llm_explanation.suggested_documents_to_review)
                )
            if f.llm_explanation.preliminary_corrective_actions:
                lines.append("- **Ações corretivas preliminares sugeridas:**")
                for act in f.llm_explanation.preliminary_corrective_actions:
                    lines.append(f"  - {act}")
            lines.append(f"- *Aviso:* {f.llm_explanation.disclaimer}")
            lines.append("")

    # Section E. Referências regulatórias
    lines.append("## E. Referências Regulatórias e Rastreabilidade Documental")
    lines.append("")
    if retrieval_trace and retrieval_trace.get("rules_retrieval"):
        lines.append(
            f"- **Modelo de Embeddings Configurado:** `{retrieval_trace.get('embedding_model_configured')}`"
        )
        lines.append(f"- **Motor de Recuperação Executado:** `{retrieval_trace.get('retrieval_backend')}`")
        lines.append("")
        lines.append("| Regra | Fragmento (`chunk_id`) | Documento | Emissor | Página/Seção | Score | Hash SHA-256 (Prefixo) | Status |")
        lines.append("|---|---|---|---|---|---|---|---|")
        for r_id, r_trace in retrieval_trace["rules_retrieval"].items():
            for ch in r_trace.get("retrieved_chunks", []):
                doc_h = (ch.get("document_hash") or "")[:12]
                lines.append(
                    f"| `{r_id}` | `{ch['chunk_id']}` | `{ch['document_id']}` | {ch['issuing_body']} | "
                    f"Pág. {ch['page']} / {ch['section_or_clause']} | `{ch['similarity_score']}` | "
                    f"`{doc_h}...` | `{ch['verification_status']}` |"
                )
        lines.append("")
    else:
        lines.append("*Recuperação RAG desabilitada nesta execução; exibindo apenas referências do catálogo estático.*")
        lines.append("")

    # Section F. Plano de ação
    lines.append("## F. Plano de Ação Preliminar Organizado por Prioridade de Revisão")
    lines.append("")
    priority_order = [
        (ReviewPriority.HIGH, "Prioridade de Revisão Alta (`high`)"),
        (ReviewPriority.MEDIUM, "Prioridade de Revisão Média (`medium`)"),
        (ReviewPriority.LOW, "Prioridade de Revisão Baixa (`low`)"),
        (ReviewPriority.INFORMATIONAL, "Informativo (`informational`)"),
    ]
    for prio_enum, prio_label in priority_order:
        matching = [f for f in report.findings if f.review_priority == prio_enum]
        if not matching:
            continue
        lines.append(f"### {prio_label}")
        for f in matching:
            lines.append(
                f"1. **{f.finding_id} ({f.rule_id} — {f.title})** [{f.status_label_pt}]: {f.recommended_action}"
            )
        lines.append("")

    return "\n".join(lines)


def write_all_outputs(
    out_dir: Path,
    report: FindingsReport,
    analysis: Dict[str, Any],
    run_manifest: Dict[str, Any],
    analysis_metrics: Dict[str, Any],
    retrieval_trace: Optional[Dict[str, Any]] = None,
) -> Dict[str, Path]:
    """Write findings.json, report.md, run_manifest.json, repository_inventory.json, analysis_metrics.json, and retrieval_trace.json."""
    out_dir = Path(out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    findings_path = out_dir / "findings.json"
    report_md_path = out_dir / "report.md"
    manifest_path = out_dir / "run_manifest.json"
    inventory_path = out_dir / "repository_inventory.json"
    metrics_path = out_dir / "analysis_metrics.json"

    findings_path.write_text(
        json.dumps(report.model_dump(mode="json"), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    inventory_payload = {
        "repository_path": analysis["repository_path"],
        "commit_sha": analysis["commit_sha"],
        "python_version": analysis["python_version"],
        "inspection_summary": analysis["inspection_summary"],
        "parsed_files": [
            {
                "file": pf["file"],
                "sha256": pf["sha256"],
                "line_count": pf["line_count"],
                "classes_count": len(pf["classes"]),
                "functions_count": len(pf["functions"]),
                "imports": pf["imports"],
            }
            for pf in analysis["parsed_files"]
        ],
        "failed_files": analysis["failed_files"],
        "standalone_model_files": analysis["standalone_model_files"],
        "dependencies": analysis["dependencies"],
        "tests_and_ci": analysis["tests_and_ci"],
    }
    inventory_path.write_text(
        json.dumps(inventory_payload, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    manifest_path.write_text(
        json.dumps(run_manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    metrics_path.write_text(
        json.dumps(analysis_metrics, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    written: Dict[str, Path] = {
        "findings_json": findings_path,
        "report_md": report_md_path,
        "run_manifest_json": manifest_path,
        "repository_inventory_json": inventory_path,
        "analysis_metrics_json": metrics_path,
    }

    if retrieval_trace is not None:
        trace_path = out_dir / "retrieval_trace.json"
        trace_path.write_text(
            json.dumps(retrieval_trace, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        written["retrieval_trace_json"] = trace_path

    md_content = render_markdown_report(
        report=report,
        analysis=analysis,
        run_manifest=run_manifest,
        retrieval_trace=retrieval_trace,
    )
    report_md_path.write_text(md_content, encoding="utf-8")

    return written

