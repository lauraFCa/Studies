import cv2, sys, os
from random import randint

# Usando GOTURN - RNA
if not (os.path.isfile('goturn.caffemodel') and os.path.isfile('goturn.prototxt')):
    print('Erro ao carregar arquivos do Goturn')
    sys.exit()

tracker = cv2.TrackerGOTURN_create()

video = cv2.VideoCapture('videos/race.mp4')
if not video.isOpened():
    print('Nao foi possivel carregar o video')
    sys.exit()

ok, frame = video.read() # primeiro frame do video
if not ok:
    print('ok=', ok)
    print( 'Nao foi possivel ler o video')
    sys.exit()

bbox = cv2.selectROI(frame, False)
ok = tracker.init(frame, bbox)


print('analisando o video')
while True:
    ok, frame = video.read()
    if not ok:
        break

    timer = cv2.getTickCount()
    ok, bbox = tracker.update(frame)
    fps = cv2.getTickCount() / (cv2.getTickCount() - timer)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,100,255), 2, 1)
    else:
        cv2.putText(frame, 'Falha no rastreamento', (100,80), cv2.FONT_HERSHEY_SIMPLEX, .75, (0,0,255), 2)
    
    cv2.putText(frame, 'Tracker GOTURN', (100,20), cv2.FONT_HERSHEY_SIMPLEX, .75, (50,170,50),2)
    cv2.putText(frame, 'FPS'+str(int(fps)), (100,20), cv2.FONT_HERSHEY_SIMPLEX, .75, (50,170,50),2)

    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0XFF == 27:
        break
