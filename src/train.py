from ultralytics import YOLO
import torch
import os

def main():
    # Für Cuda Training 
    device = 0 if torch.cuda.is_available() else "cpu"
    
    my_model_path = "models/yolo_train/weights/best.pt"
    
    if not os.path.exists(my_model_path) or os.path.getsize(my_model_path) == 0:
        print("Kein eigenes Modell gefunden. Starte mit YOLOv8l Basis-Modell...")
        model = YOLO("yolov8l.pt") 
    else:
        print(f"Lade existierendes Modell: {my_model_path}")
        model = YOLO(my_model_path)

    model.train(
        data="dataset/config.yaml", 
        epochs=15,
        imgsz=640, 
        device=device,
        workers=2,
        project="models", 
        name="yolo_train",
        exist_ok=True,
        patience=5
    )

if __name__ == "__main__":
    main()