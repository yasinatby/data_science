# YOLO Detection Project

## Projektstruktur
Dieses Projekt enthält:
- Datensatzstruktur für Training und Validierung
- YOLO-Modell unter `models/best.pt`
- Video-Eingabe und Ausgabeordner
- Python-Skripte für Training und Video-Erkennung
- Flask-Webanwendung
- Docker-Setup

## Start
```bash
pip install -r requirements.txt
python webapp/app.py
```

## Detection ausführen
```bash
python src/detect_video.py
```
