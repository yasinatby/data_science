from ultralytics import YOLO

def main():
    model = YOLO("models/best.pt")
    results = model.predict(
        source="videos/input.mp4",
        save=True,
        project="outputs",
        name="predict"
    )
    print("Video detection completed.")

if __name__ == "__main__":
    main()
