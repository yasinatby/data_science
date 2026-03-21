# YOLO Video Detection & Training

YOLO-basierte Computer Vision App mit **Training** und **Detection** in 2 Docker Containern.

## Was macht das Projekt?

- **Detection**: Videos hochladen → YOLO erkennt Objekte → Ausgabe mit Bounding Boxes
- **Training**: Custom YOLO Modelle mit eigenem Dataset trainieren
- **Docker**: 2 separate Container für beide Tasks

## Docker Container

**Wichtig:** Wähle die richtige Datei für dein System!

### Mac M2/M1 (CPU-only)
```bash
docker-compose -f docker-compose.mac.yaml up --build
```

### Windows/Linux mit RTX GPU
```bash
docker-compose -f docker-compose.win.yaml up --build
```

### Services starten (einzeln)

**Training Container:**
```bash
docker-compose -f docker-compose.win.yaml up train
```
- Trainiert YOLO mit Daten aus `dataset/`
- Speichert beste Gewichte in `models/best.pt`
- GPU wird automatisch erkannt (falls verfügbar)

**Web Detection Server:**
```bash
docker-compose -f docker-compose.win.yaml up web
```
- FastAPI Webserver auf http://localhost:8000
- Videos hochladen → YOLO Detection
- Ergebnisse in `outputs/`

## Quick Start

### Lokal (ohne Docker):
```bash
pip install -r requirements.txt
python src/train.py                    # Modell trainieren
python src/detect_video.py             # Video Detection
```

### Mit Docker (entscheide anhand deines Systems):

**Mac M2/M1:**
```bash
docker-compose -f docker-compose.mac.yaml up --build
```

**Windows/Linux mit NVIDIA GPU:**
```bash
docker-compose -f docker-compose.win.yaml up --build
```

### Container verwalten:

**Stoppen & löschen:**
```bash
docker-compose -f docker-compose.mac.yaml down
docker-compose -f docker-compose.win.yaml down
```

**Nur stoppen (nicht löschen):**
```bash
docker-compose -f docker-compose.mac.yaml stop
docker-compose -f docker-compose.win.yaml stop
```

**Wieder starten:**
```bash
docker-compose -f docker-compose.mac.yaml start
docker-compose -f docker-compose.win.yaml start
```

### Training im Container starten:
```bash
docker exec data_science-train-1 python src/train.py
```

### Logs ansehen:
```bash
docker-compose -f docker-compose.win.yaml logs web
docker-compose -f docker-compose.win.yaml logs train
```

### In Container gehen (bash):
```bash
docker exec -it data_science-web-1 bash
docker exec -it data_science-train-1 bash
```

## System Anforderungen

**Lokal (ohne Docker):**
- Python 3.10+
- PyTorch (cpu oder gpu)
- OpenCV, Ultralytics

**Mit Docker:**
- Docker + Docker Compose
- Mac M2/M1: `docker-compose.mac.yaml` (CPU-only, funktioniert überall)
- Windows/Linux + NVIDIA GPU: `docker-compose.win.yaml` (mit GPU-Support)
- NVIDIA Container Toolkit (falls GPU gewünscht)

**GPU optional:**
Falls die RTX 3050 erkannt wird, beschleunigt sich Training um 3-5x

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
