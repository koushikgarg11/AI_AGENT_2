import streamlit as st
import os
import time
from datetime import datetime

st.set_page_config(page_title="ACC Mock Interview Prototype")
st.title("AnalyticsCareerConnect — Mock Interview Prototype")

user = st.text_input("Your name (optional)")
role = st.selectbox("Role", ["Data Analyst", "Data Scientist", "ML Engineer", "Business Analyst"])
mode = st.radio("Mode", ["Typed answer", "Upload audio (MP3/WAV)"])

question = "Tell me about a time you used data to influence a decision."

st.subheader("Question")
st.write(question)

if mode == "Typed answer":
    answer = st.text_area("Your answer", height=200)
else:
    audio = st.file_uploader("Upload audio file", type=["wav", "mp3", "m4a"])

if st.button("Submit"):
    st.info("Submitting...")
    os.makedirs("data", exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    uid = (user or "anon").replace(" ", "_")

    if mode == "Typed answer":
        path = f"data/{uid}_{timestamp}.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(answer or "")
    else:
        if audio is None:
            st.error("Please upload an audio file.")
            st.stop()
        path = f"data/{uid}_{timestamp}_" + audio.name
        with open(path, "wb") as f:
            f.write(audio.getbuffer())

    with st.spinner("Processing (simulated)..."):
        time.sleep(2)

    if mode == "Typed answer":
        words = len((answer or "").split())
        fillers = sum((answer or "").lower().count(w) for w in ["um", "uh", "like", "you know"]) 
        score = max(30, min(90, 50 + (words - 50) // 2 - fillers * 5))
        st.success(f"Automated feedback — score: {score}/100")
        st.write(f"Word count: {words}, filler words: {fillers}")
        st.markdown("**Suggestions:** Speak with structure (STAR), avoid filler words, add concrete metrics.")
    else:
        st.success("Audio received. Transcription & feedback would appear here (placeholder).")

    if st.button("Request coach review"):
        st.info("Coach review requested (placeholder).")

st.markdown("---")
st.caption("Prototype: records saved to ./data. Integrate transcription and LLM feedback next.")
