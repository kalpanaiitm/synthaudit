import re

from .guardrails import screen_text
from .models import AuditReport, CheckResult
from .preprocessing import split_method_text
from .rules import CHECKS

SCOPE_NOTICE = (
    "Reporting-completeness screen only. This is not a determination of reproducibility, "
    "scientific validity, chemical safety, or regulatory compliance. Expert review is required."
)


def _evidence(text: str, patterns: list[str]) -> list[str]:
    hits: list[str] = []
    for pattern in patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            snippet = re.sub(r"\s+", " ", text[max(0, match.start() - 45):match.end() + 45]).strip()
            if snippet not in hits:
                hits.append(snippet)
            if len(hits) == 2:
                return hits
    return hits


def audit_text(text: str) -> AuditReport:
    guardrails = screen_text(text)
    if not guardrails.input_allowed:
        return AuditReport(
            score=0, chunk_count=0, checks=[], missing=[], guardrails=guardrails, scope_notice=SCOPE_NOTICE
        )

    chunks = split_method_text(text)
    results: list[CheckResult] = []
    earned = 0
    total = sum(item["weight"] for item in CHECKS.values())
    for field, rule in CHECKS.items():
        evidence: list[str] = []
        for chunk in chunks:
            for snippet in _evidence(chunk, rule["patterns"]):
                if snippet not in evidence:
                    evidence.append(snippet)
                if len(evidence) == 2:
                    break
            if len(evidence) == 2:
                break
        status = "reported" if evidence else "not_detected"
        if evidence:
            earned += rule["weight"]
        results.append(CheckResult(
            field=field, label=rule["label"], status=status,
            evidence=evidence, weight=rule["weight"],
        ))
    score = round(100 * earned / total)
    missing = [result.label for result in results if result.status == "not_detected"]
    return AuditReport(
        score=score, chunk_count=len(chunks), checks=results, missing=missing,
        guardrails=guardrails, scope_notice=SCOPE_NOTICE,
    )
