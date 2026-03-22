from ultralytics import YOLO
import cv2
import torch
from pathlib import Path

#Hardware Detection 0 Nvdiea else Mac
DEVICE = 0 if torch.cuda.is_available() else "cpu"
print(f"🚀 Initialisiere Hardware: {DEVICE}")

def detect_on_video(video_path, model_path="models/best.pt"):
    """
    TODO: Implementiere die Objekterkennung.
    Nutze 'DEVICE' beim Laden des Modells oder beim Predict-Aufruf.
    """
    model = YOLO(model_path)

    # results = model.track(source=str(video_path), stream=True, device=DEVICE)
    pass

def annotate_frame(frame, results, model):
    """
    TODO: Zeichne Bounding Boxes und Labels manuell oder via YOLO auf das Frame.
    """
    pass

def save_video_with_detections(input_path, output_path, model_path="models/best.pt"):
    """
    TODO: Lade das Video mit cv2.VideoCapture, loope durch die Frames,
    rufe detect_on_video auf und speichere mit cv2.VideoWriter.
    """
    pass

def main():
    """CLI interface für die Video-Erkennung"""
   
    input_vid = Path("videos/input.mp4")
    output_vid = Path("outputs/result.mp4")
    
    print(f"Programm gestartet auf: {DEVICE}")
    
    pass

if __name__ == "__main__":
    main()