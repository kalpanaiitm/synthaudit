from synthaudit import audit_text


def test_complete_fictional_example_detects_core_fields():
    text = (
        "A nitrate precursor (1 mmol) was dispersed in 20 mL water and heated at 180 °C "
        "for 12 hours under nitrogen. After cooling, it was washed and dried. XRD was recorded."
    )
    report = audit_text(text)
    assert report.guardrails.input_allowed
    assert report.score >= 75
    assert report.chunk_count >= 1
    assert any(item.field == "temperature" and item.status == "reported" for item in report.checks)


def test_empty_input_is_blocked():
    report = audit_text("   ")
    assert not report.guardrails.input_allowed
    assert report.score == 0
    assert report.chunk_count == 0


def test_long_text_is_split_into_multiple_chunks():
    text = ("The precursor was mixed with water and characterised by XRD. " * 80)
    report = audit_text(text)
    assert report.chunk_count > 1


def test_sensitive_and_higher_risk_language_warns_without_advice():
    report = audit_text("Unpublished work: contact scientist@example.com about a pyrophoric reagent.")
    assert report.guardrails.input_allowed
    assert len(report.guardrails.warnings) == 2


def test_input_limit_is_enforced():
    report = audit_text("x" * 12_001)
    assert not report.guardrails.input_allowed
