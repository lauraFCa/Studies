import cv2, sys
from random import randint

tracker = cv2.TrackerCSRT_create()

video = cv2.VideoCapture('videos/walking.avi')
if not video.isOpened():
    print('Nao foi possivel abrir o video')
    sys.exit()

ok, frame = video.read()
if not ok:
    print('Nao e possivel ler o arquivo de video')
    sys.exit()

# usar o cascade para detectar uma pessoa no primeiro frame do video
cascade = cv2.CascadeClassifier('cascade/fullbody.xml')

def detectar():
    while True:
        ok, frame = video.read()
        cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detection = cascade.detectMultiScale(cinza)
        for (x, y, l, a) in detection:
            cv2.rectangle(frame, (x,y), (x+l, y+a), (0,0,255), 2)
            cv2.imshow('Deteccao', frame)
            
            if x > 0:
                print('Deteccao efetuada pelo haarcascade')
                return x, y, l, a

bbox = detectar()

ok = tracker.init(frame, bbox)
colors = ( randint(0,255),randint(0,255),randint(0,255) )

while True:
    ok, frame = video.read()
    if not ok:
        break

    ok, bbox = tracker.update(frame) # quando rastreador falha ok=False - roda detector
    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x,y), (x+w, y+h), colors, 2,1)
    else:
        print('Falha no rastreamento - executando Detector haarcascade')
        bbox = detectar()
        tracker = cv2.TrackerMOSSE_create()
        tracker.init(frame, bbox)

    cv2.imshow('Tracking', frame)
    k=cv2.waitKey(1) & 0XFF
    if k == 27:
        break
