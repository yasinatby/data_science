from ultralytics import YOLO

def main():
   
    model = YOLO("yolov8l.pt")  
    model.train(data="dataset/config.yaml", epochs=50, imgsz=640)

if __name__ == "__main__":
    main()
