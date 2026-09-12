from typing import Literal

from pydantic import BaseModel, Field


class CheckResult(BaseModel):
    field: str
    label: str
    status: Literal["reported", "not_detected"]
    evidence: list[str] = Field(default_factory=list)
    weight: int


class GuardrailResult(BaseModel):
    input_allowed: bool
    warnings: list[str] = Field(default_factory=list)


class AuditReport(BaseModel):
    score: int = Field(ge=0, le=100)
    chunk_count: int = Field(default=0, ge=0)
    checks: list[CheckResult]
    missing: list[str]
    guardrails: GuardrailResult
    scope_notice: str
