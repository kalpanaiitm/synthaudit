import re

from .models import GuardrailResult

MAX_CHARS = 12_000

SENSITIVE_PATTERNS = [
    r"\bconfidential\b",
    r"\bunpublished\b",
    r"\bpatent pending\b",
    r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
]

HIGHER_RISK_TERMS = [
    "explosive", "detonation", "peroxide", "cyanide", "azide",
    "pyrophoric", "radioactive", "high pressure", "hydrofluoric",
]


def screen_text(text: str) -> GuardrailResult:
    warnings: list[str] = []
    stripped = text.strip()
    if not stripped:
        return GuardrailResult(input_allowed=False, warnings=["Enter experimental text to run an audit."])
    if len(text) > MAX_CHARS:
        return GuardrailResult(
            input_allowed=False,
            warnings=[f"Input exceeds the {MAX_CHARS:,}-character public-demo limit."],
        )
    if any(re.search(pattern, text, re.IGNORECASE) for pattern in SENSITIVE_PATTERNS):
        warnings.append(
            "Possible personal, confidential, or unpublished information detected. Remove it before continuing."
        )
    found = sorted({term for term in HIGHER_RISK_TERMS if term in text.lower()})
    if found:
        warnings.append(
            "Higher-risk chemistry language was detected. This tool provides no safety assessment or procedural advice; "
            "use institutional risk assessment and qualified supervision."
        )
    return GuardrailResult(input_allowed=True, warnings=warnings)
