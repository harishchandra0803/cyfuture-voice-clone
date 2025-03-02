import streamlit as st
import requests

st.title("🎤 Voice Cloning & TTS App")

# **📌 Text-to-Speech & Audio Upload in One Place**
st.header("🗣️ Generate or Upload Audio")

# **Text-to-Speech Input**
text = st.text_area("Enter text for Text-to-Speech", "Hello, this is a TTS demo.")

# **Audio Upload Input**
uploaded_file = st.file_uploader("Or upload an audio file (MP3/WAV)", type=["mp3", "wav"])

# **Generate Speech Button**
if st.button("Generate Speech 🎵"):
    if text:
        response = requests.get("http://127.0.0.1:8000/tts/", params={"text": text})
        
        if response.status_code == 200:
            st.audio(response.content, format="audio/mp3")  # Play audio
            st.success("✅ TTS conversion completed!")
        else:
            st.error("🚨 Failed to generate speech.")
    else:
        st.warning("⚠️ Please enter some text!")

# **Upload & Process Audio**
if uploaded_file:
    st.audio(uploaded_file, format="audio/mp3")  # Preview uploaded audio

    # Send to backend for processing
    files = {"file": uploaded_file.getvalue()}
    response = requests.post("http://127.0.0.1:8000/upload_audio/", files=files)

    if response.status_code == 200:
        st.success("✅ Audio uploaded successfully!")
    else:
        st.error("🚨 Failed to upload audio.")
