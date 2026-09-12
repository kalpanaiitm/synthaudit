# SynthAudit

SynthAudit is a free, open-source **materials synthesis reporting-completeness checker**. It extracts reported experimental details, identifies missing categories, and creates an auditable human-review checklist.

It is designed as a portfolio-quality research software demonstration. It does **not** validate scientific correctness, reproduce an experiment, assess chemical safety, or recommend synthesis conditions.

## What it checks

- precursors and quantities
- solvent and volume
- temperature and duration
- atmosphere, pressure, and pH
- cooling, washing, and drying
- characterisation methods

Longer methods text is preprocessed with LangChain's `RecursiveCharacterTextSplitter`, using bounded overlapping chunks. No LLM, embedding service, or external API is called.

## Guardrails

- deterministic rules: no generative AI or paid API
- LangChain text splitting without sending content to an external service
- no file uploads in the public MVP
- input capped at 12,000 characters
- text is processed only in the active Streamlit session
- warning for possible personal/confidential information
- warning for higher-risk chemistry language
- no hazardous procedural recommendations
- results require expert human review
- fictional example included; do not paste unpublished or sensitive work

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Test

```bash
pytest -q
```

## Deployment

Deploy `app.py` from the repository's `main` branch on Streamlit Community Cloud. No secrets are required.

## Responsible-use scope

SynthAudit assesses whether categories of information appear to be reported. Keyword and pattern matching can produce false positives and false negatives. Its score is not evidence of reproducibility, validity, quality, regulatory compliance, or laboratory safety. Users remain responsible for institutional procedures, risk assessments, supervision, and expert review.

## Licence

MIT. See `LICENSE`.
