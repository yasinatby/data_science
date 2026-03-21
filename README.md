# YOLO Video Detection & Training

YOLO-basierte Computer Vision App mit **Training** und **Detection** in 2 Docker Containern.

## Was macht das Projekt?

- **Detection**: Videos hochladen → YOLO erkennt Objekte → Ausgabe mit Bounding Boxes
- **Training**: Custom YOLO Modelle mit eigenem Dataset trainieren
- **Docker**: 2 separate Container für beide Tasks

## Docker Container

### 1. `train` - Modell trainieren
```bash
docker-compose up train
```
- Trainiert YOLO mit `dataset/`
- Speichert beste Gewichte in `models/best.pt`
- GPU wird automatisch erkannt

### 2. `web` - Detection Webapp
```bash
docker-compose up web
```
- FastAPI Webserver auf http://localhost:8000
- Videos hochladen → Detection läuft
- Ergebnisse in `outputs/`

## Quick Start

**Lokal (ohne Docker):**
```bash
pip install -r requirements.txt
python src/train.py                    # Training
python src/detect_video.py --source video.mp4  # Detection
```

**Mit Docker - Mac M2/M1:**
```bash
docker-compose -f docker-compose.mac.yaml up --build
```

**Mit Docker - Windows/Linux mit RTX GPU:**
```bash
docker-compose -f docker-compose.win.yaml up --build
```

**Container herunterfahren:**
```bash
# Beide Container stoppen und löschen
docker-compose -f docker-compose.mac.yaml down
docker-compose -f docker-compose.win.yaml down

# Nur stoppen (ohne zu löschen)  
docker-compose -f docker-compose.mac.yaml stop
docker-compose -f docker-compose.win.yaml stop
```

## Anforderungen
- Python 3.10 + CUDA 12.8 (optional für GPU)
- Docker + Docker Compose

## Struktur
```
├── dataset/         → Trainingsdaten (Bilder + Labels)
├── models/          → YOLO Gewichte
├── src/
│   ├── train.py     → Training Script
│   └── detect_video.py → Detection Script
├── webapp/app.py    → FastAPI Detection Server
├── outputs/         → Inference Ergebnisse
└── videos/          → Hochgeladene Videos
```
