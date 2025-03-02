from fastapi import FastAPI, UploadFile, File
from gtts import gTTS
import os
from fastapi.responses import FileResponse

app = FastAPI()

# Ensure output directory exists
os.makedirs("backend/audio", exist_ok=True)

# 🎤 **TEXT-TO-SPEECH API**
@app.get("/tts/")
def text_to_speech(text: str):
    audio_path = "backend/audio/output.mp3"
    tts = gTTS(text)
    tts.save(audio_path)
    return FileResponse(audio_path, media_type="audio/mpeg", filename="output.mp3")

# 📂 **AUDIO UPLOAD API**
@app.post("/upload_audio/")
async def upload_audio(file: UploadFile = File(...)):
    file_location = f"backend/audio/{file.filename}"
    
    # Save the uploaded audio
    with open(file_location, "wb") as f:
        f.write(await file.read())
    
    return {"message": "Audio uploaded successfully", "file_path": file_location}
