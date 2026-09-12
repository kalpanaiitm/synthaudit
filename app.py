import json

import streamlit as st

from synthaudit import audit_text
from synthaudit.guardrails import MAX_CHARS

SAMPLE = """Fictional demonstration only. A metal nitrate precursor (1.25 mmol) and a metal oxide (0.50 g)
were dispersed in 25 mL water. The mixture was heated at 180 °C for 12 hours under nitrogen.
After cooling to room temperature, the solid was filtered, washed with water and ethanol, and dried.
Powder XRD and SEM were used for characterisation."""

st.set_page_config(page_title="SynthAudit", page_icon="🧪", layout="wide")
st.title("🧪 SynthAudit")
st.subheader("Materials synthesis reporting-completeness checker")
st.info(
    "Free public demonstration. It checks whether reporting categories appear in text; it does not "
    "validate an experiment, assess safety, or recommend conditions."
)

with st.sidebar:
    st.header("Responsible use")
    st.markdown(
        "- Use fictional, published, or your own non-sensitive text\n"
        "- Remove names, email addresses and confidential details\n"
        "- Do not rely on this app for laboratory safety\n"
        "- A qualified person must review every result"
    )
    acknowledged = st.checkbox("I understand these limitations")
    use_sample = st.button("Load fictional example")

if "audit_text" not in st.session_state:
    st.session_state.audit_text = ""
if use_sample:
    st.session_state.audit_text = SAMPLE

text = st.text_area(
    "Paste an experimental synthesis description",
    key="audit_text",
    height=240,
    max_chars=MAX_CHARS,
    help=f"Maximum {MAX_CHARS:,} characters. The app does not intentionally persist this text.",
)
st.caption(f"{len(text):,} / {MAX_CHARS:,} characters")

if st.button("Run completeness audit", type="primary", disabled=not acknowledged):
    report = audit_text(text)
    for warning in report.guardrails.warnings:
        st.warning(warning)
    if report.guardrails.input_allowed:
        st.metric("Reporting completeness score", f"{report.score}%")
        st.caption(f"Analysed across {report.chunk_count} traceable text chunk(s).")
        st.caption("A heuristic coverage score—not a quality, safety, or reproducibility rating.")
        st.progress(report.score / 100)
        left, right = st.columns(2)
        with left:
            st.subheader("Detected categories")
            for check in report.checks:
                if check.status == "reported":
                    with st.expander(f"✅ {check.label}"):
                        for item in check.evidence:
                            st.write(item)
        with right:
            st.subheader("Human-review checklist")
            if report.missing:
                for label in report.missing:
                    st.write(f"⚠️ Confirm whether **{label}** should be reported.")
            else:
                st.success("All configured categories were detected. Expert review is still required.")
        st.error(report.scope_notice)
        st.download_button(
            "Download JSON audit report",
            data=json.dumps(report.model_dump(), indent=2),
            file_name="synthaudit_report.json",
            mime="application/json",
        )

with st.expander("Privacy and limitations"):
    st.write(
        "Text is processed in the active application session and is not intentionally written to a database. "
        "Hosting infrastructure may still create operational logs. Do not submit confidential, personal, "
        "export-controlled, proprietary, or unpublished information. Pattern matching may miss information "
        "or detect it incorrectly."
    )
