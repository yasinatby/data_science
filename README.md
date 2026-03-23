# YOLO Video Detection & Training

YOLO-basierte Computer Vision App mit **Training** und **Detection** in 2 Docker Containern.

## Was macht das Projekt?

- **Detection**: Videos hochladen → YOLO erkennt Objekte → Ausgabe mit Bounding Boxes
- **Training**: Custom YOLO Modelle mit eigenem Dataset trainieren
- **Docker**: 2 separate Container für beide Tasks


## Docker 

docker compose 


## Wichtige CMD

Um Graphen zu visualisieren: 

tensorboard --logdir ultralytics/runs # replace with 'runs' directory


## Objekt Klassen für YOLO 

0  Player
1  Goalkeepers
2  Referee
3  Ball
4  Corner
5  Goal
