AnalyticsCareerConnect — Mock Interview Agent (prototype)

This repository contains a Streamlit prototype and a minimal FastAPI backend for an Interview Prep / Mock Interview agent for analyticscareerconnect.com.

Quickstart (local)
1. Create a virtualenv: python -m venv .venv
2. Activate it and install deps: pip install -r requirements.txt
3. Run Streamlit UI: streamlit run streamlit_app.py
4. (Optional) Run backend: uvicorn backend.app:app --reload

What’s included
- streamlit_app.py: Prototype UI for typed/ uploaded answers and simulated automated feedback
- backend/app.py: FastAPI stub with endpoints for starting mocks and uploading audio
- .github/workflows/ci.yaml: CI workflow to install deps and run a smoke import

Next steps
- Implement audio recording Streamlit component
- Integrate transcription (Whisper or API) and LLM-based feedback
- Add persistent DB, object storage, and authentication
