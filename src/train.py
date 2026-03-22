from ultralytics import YOLO
import torch

def main():
    # Für Cuda Training 
    device = 0 if torch.cuda.is_available() else "cpu"

    model = YOLO("yolov8l.pt")  
    
   
    model.train(
        data="dataset/config.yaml", 
        epochs=50, 
        imgsz=640, 
        device=device,
        workers=4 
    )

if __name__ == "__main__":
    main()