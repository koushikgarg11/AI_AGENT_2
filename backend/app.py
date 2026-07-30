from fastapi import FastAPI, UploadFile, File
import os

app = FastAPI()
os.makedirs("data", exist_ok=True)

@app.post("/api/v1/mock/start")
async def start_mock(user_id: str = "anon", role: str = "Data Analyst", difficulty: str = "medium"):
    return {"mock_id": "mock_123", "question": "Tell me about a time you used data to influence a decision."}

@app.post("/api/v1/mock/{mock_id}/upload-audio")
async def upload_audio(mock_id: str, file: UploadFile = File(...)):
    path = f"data/{mock_id}_{file.filename}"
    with open(path, "wb") as f:
        f.write(await file.read())
    return {"status": "ok", "path": path}

@app.post("/api/v1/mock/{mock_id}/process")
async def process_mock(mock_id: str):
    # enqueue transcription & feedback in production
    return {"status": "processing", "mock_id": mock_id}

@app.get("/api/v1/mock/{mock_id}/status")
async def status(mock_id: str):
    return {"mock_id": mock_id, "transcript_ready": False, "feedback_ready": False}
