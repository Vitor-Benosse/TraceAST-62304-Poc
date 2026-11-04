"""Pydantic schemas for TraceAST-62304 findings, rules, inventory, RAG trace, and manifests."""

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, model_validator


class FindingStatus(str, Enum):
    OBSERVED = "observed"
    NOT_OBSERVED = "not_observed"
    PARTIAL = "partial"
    UNABLE_TO_ASSESS = "unable_to_assess"
    NOT_APPLICABLE = "not_applicable"


class ReviewPriority(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFORMATIONAL = "informational"


class ConfidenceLevel(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class MappingStatus(str, Enum):
    PENDING_EXPERT_REVIEW = "pending_expert_review"
    REVIEWED = "reviewed"
    APPROVED_BY_EXPERT = "approved_by_expert"
    UNVERIFIED = "unverified"


class ProductProfile(BaseModel):
    name: str = Field(default="Unknown Medical Software Project")
    intended_purpose: str = Field(default="unknown")
    intended_users: str = Field(default="unknown")
    target_market: List[str] = Field(default_factory=lambda: ["Brazil"])
    software_type: str = Field(default="unknown")
    ai_components: Optional[bool] = Field(default=None)
    clinical_decision_context: str = Field(default="unknown")
    profile_source_path: Optional[str] = Field(default=None)
    profile_limitations: List[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def evaluate_unknown_fields(self) -> "ProductProfile":
        limitations = list(self.profile_limitations)
        unknown_markers = {"", "unknown", "desconhecido", "n/a", "none", "tbd"}
        if self.intended_purpose.strip().lower() in unknown_markers:
            msg = (
                "Finalidade médica pretendida (intended_purpose) não informada ou desconhecida. "
                "O sistema não infere finalidade clínica pelos nomes de classes ou funções; "
                "a contextualização regulatória requer revisão humana."
            )
            if msg not in limitations:
                limitations.append(msg)
        if self.clinical_decision_context.strip().lower() in unknown_markers:
            msg = (
                "Contexto de decisão clínica (clinical_decision_context) desconhecido. "
                "Impossível contextualizar o impacto operacional sem definição formal pelo fabricante."
            )
            if msg not in limitations:
                limitations.append(msg)
        if self.ai_components is None:
            msg = (
                "Presença de componentes de IA (ai_components) não declarada no perfil; "
                "regras de ML serão avaliadas apenas por sinais estruturais no código."
            )
            if msg not in limitations:
                limitations.append(msg)
        self.profile_limitations = limitations
        return self


class EvidenceItem(BaseModel):
    file: str = Field(..., description="Relative path of the file inside the repository")
    symbol: Optional[str] = Field(default=None, description="Class, function, or method name when applicable")
    line_start: Optional[int] = Field(default=None, ge=1, description="Starting line number (1-indexed)")
    line_end: Optional[int] = Field(default=None, ge=1, description="Ending line number (1-indexed)")
    evidence_type: str = Field(..., description="Type of structural evidence extracted")
    description: str = Field(..., description="Description of the evidence and related rule context")
    metadata: Dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def validate_lines(self) -> "EvidenceItem":
        if self.line_start is not None and self.line_end is not None:
            if self.line_end < self.line_start:
                raise ValueError(f"line_end ({self.line_end}) cannot be less than line_start ({self.line_start})")
        return self


class RegulatoryReference(BaseModel):
    document_id: str = Field(..., description="Identifier of the regulatory document (e.g., IEC62304, ANVISA_RDC_657_2022)")
    document_name: str = Field(default="", description="Official or template document title")
    issuing_body: str = Field(default="", description="Issuing institution (e.g., IEC, ANVISA, OpenRegulatory)")
    clause: Optional[str] = Field(default=None, description="Verifiable clause or section identifier")
    section_or_page: Optional[str] = Field(default=None, description="Original page or section reference")
    mapping_status: MappingStatus = Field(default=MappingStatus.PENDING_EXPERT_REVIEW)
    source: Optional[str] = Field(default=None, description="Relative path or URL of the reference document")
    chunk_id: Optional[str] = Field(default=None, description="Retrieved RAG fragment identifier")
    similarity_score: Optional[float] = Field(default=None, description="Similarity score from vector/hybrid retrieval")
    excerpt: Optional[str] = Field(default=None, description="Retrieved text excerpt when permissible")
    document_hash: Optional[str] = Field(default=None, description="SHA-256 hash of the source document")


class LLMExplanationOutput(BaseModel):
    accessible_explanation: str = Field(..., description="Plain-language explanation of the technical finding")
    suggested_documents_to_review: List[str] = Field(default_factory=list)
    preliminary_corrective_actions: List[str] = Field(default_factory=list)
    disclaimer: str = Field(
        default="Explicação complementar gerada por IA. Revisão humana necessária; não altera o status determinístico."
    )


class Finding(BaseModel):
    finding_id: str = Field(..., pattern=r"^TA-\d{3}$")
    rule_id: str = Field(..., pattern=r"^R\d{2}$")
    title: str
    category: str
    status: FindingStatus
    status_label_pt: str = Field(..., description="Standardized Portuguese regulatory screening expression")
    review_priority: ReviewPriority
    confidence: ConfidenceLevel
    description: str
    justification: str = Field(..., description="Explicit trace justification or applicability rationale")
    evidence: List[EvidenceItem] = Field(default_factory=list)
    regulatory_references: List[RegulatoryReference] = Field(default_factory=list)
    limitations: List[str] = Field(..., min_length=1)
    recommended_action: str
    human_review_required: bool = Field(default=True)
    llm_explanation: Optional[LLMExplanationOutput] = Field(default=None)

    @model_validator(mode="after")
    def validate_finding_consistency(self) -> "Finding":
        if not self.evidence and not self.justification.strip():
            raise ValueError(f"Finding {self.finding_id} must have either evidence or an explicit justification.")
        if self.status == FindingStatus.NOT_APPLICABLE and not self.justification.strip():
            raise ValueError(f"Finding {self.finding_id} with status not_applicable requires a justification.")
        return self


class RuleDefinition(BaseModel):
    rule_id: str = Field(..., pattern=r"^R\d{2}$")
    version: str = Field(default="1.0.0")
    title: str
    description: str
    objective: str
    category: str
    evidence_sought: str
    detection_method: str
    analyzed_files_scope: str
    identification_criteria: str
    limitations: List[str]
    default_review_priority: ReviewPriority
    normative_references: List[RegulatoryReference]
    regulatory_validation_status: MappingStatus = Field(default=MappingStatus.PENDING_EXPERT_REVIEW)
    rag_query_pt: str
    rag_query_en: str


class FindingsReport(BaseModel):
    schema_version: str = Field(default="1.0.0")
    tool_name: str = Field(default="TraceAST-62304")
    tool_version: str = Field(default="1.0.0")
    positioning: str = Field(
        default="AI-assisted, evidence-traceable pre-audit screening for medical software development repositories."
    )
    project_name: str
    commit_sha: Optional[str]
    execution_timestamp: str
    product_profile: ProductProfile
    findings: List[Finding]
    summary_counts: Dict[str, int]
    mandatory_disclaimers: List[str]

