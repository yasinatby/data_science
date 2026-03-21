from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from ultralytics import YOLO
import os
import shutil
from pathlib import Path
from src.detect_video import save_video_with_detections

app = FastAPI()

# Global model cache (lazy loading)
_model = None
MODEL_PATH = "models/best.pt"

def get_model():
    """Load model lazily (only when needed)"""
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model nicht gefunden: {MODEL_PATH}")
        print(f"Lade Modell von {MODEL_PATH}...")
        _model = YOLO(MODEL_PATH)
    return _model

# Mount templates folder for serving static HTML
template_dir = Path(__file__).parent / "templates"

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "model_loaded": _model is not None}

@app.get("/", response_class=HTMLResponse)
async def get_form():
    """Render the upload form"""
    with open(template_dir / "index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/upload", response_class=HTMLResponse)
async def upload_video(video: UploadFile = File(...)):
    """Handle video upload and detection"""
    try:
        model = get_model()  # Lazy load model
        
        # Save uploaded file
        upload_path = "videos/uploaded.mp4"
        os.makedirs("videos", exist_ok=True)
        
        with open(upload_path, "wb") as buffer:
            shutil.copyfileobj(video.file, buffer)
        
        # Run YOLO detection
        save_video_with_detections(
            input_path=upload_path,
            output_path="outputs/web_predict.mp4",
            model_path=MODEL_PATH
        )
        result_path = "outputs/web_predict.mp4"
        
        # Return result HTML
        with open(template_dir / "index.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        html_content += f"\n<p>Verarbeitung abgeschlossen. Ausgabe gespeichert unter: {result_path}</p>"
        return html_content
    except FileNotFoundError as e:
        return f"<p>Fehler: {str(e)} — Bitte trainiere erst ein Modell!</p>"
    except Exception as e:
        return f"<p>Fehler: {str(e)}</p>"
