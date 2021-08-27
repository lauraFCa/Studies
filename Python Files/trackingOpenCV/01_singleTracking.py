import cv2
import sys
from random import randint

print(cv2.__version__)
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.') # divide a versao do opencv nos pontos
#print(major_ver, '##', minor_ver, '##', subminor_ver)

tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']

tracker_type = tracker_types[0] 
if int(minor_ver) < 3:
    print('OpenCV com subversao menor que 3')
    tracker = tracker_type
else:
    if tracker_type == 'BOOSTING':
        tracker = cv2.TrackerBoosting_create()
    elif tracker_type == 'MIL':
        tracker = cv2.TrackerMIL_create()
    elif tracker_type == 'KCF':
        tracker = cv2.TrackerKCF_create()
    elif tracker_type == 'TLD':
        tracker = cv2.TrackerTLD_create()
    elif tracker_type == 'MEDIANFLOW':
        tracker = cv2.TrackerMedianFlow_create()
    elif tracker_type == 'MOSSE':
        tracker = cv2.TrackerMOSSE_create()
    elif tracker_type == 'CSRT':
        tracker = cv2.TrackerCSRT_create()

video = cv2.VideoCapture('videos/LED2.mp4')
if not video.isOpened():
    print('Nao foi possivel carregar o video')
    sys.exit()

ok, frame = video.read() # ok indica se foi possivel ler o video, frame e a img
if not ok:
    print('ok=', ok)
    print( 'Nao foi possivel ler o video')
    sys.exit()

bbox = cv2.selectROI(frame, False) # seleciona regiao de interesse
# bbox = (x, y, alturaBBOX, larguraBBOX)
# inicializar o video com a caixa

ok = tracker.init(frame, bbox) # primeiro frame que comeca o rastreio, bbox=objeto rastreado
# se Ok = True, conseguiu fazer a inicializacao

colors = (randint(0,255), randint(0,255), randint(0,255)) #uso pra multiplos trackings BGR
vetor_bbox=[]
print('analisando o video')
while True:
    ok, frame = video.read()
    if not ok:
        # acabou de percorrer todo o video, vai para execucao
        break

    # medir FPS, para saber desempenho (frame por segundo)
    timer = cv2.getTickCount() # retorna num de ciclo de clock apos um evento
    ok, bbox = tracker.update(frame) # cada frame do video - ok=indica se conseguiu ler
    # se objeto sofre oclusao, ok fica False
    vetor_bbox.append(bbox)
    fps = cv2.getTickCount() / (cv2.getTickCount() - timer)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x,y), (x+w, y+h), colors, 2, 1)
    else:
        cv2.putText(frame, 'Falha no rastreamento', (100,20), cv2.FONT_HERSHEY_SIMPLEX, .75, (0,0,255), 2)
    
    cv2.putText(frame, tracker_type+' Tracker', (100,50), cv2.FONT_HERSHEY_SIMPLEX, .75, (50,170,50),2)
    cv2.putText(frame, 'FPS'+str(int(fps)), (100,80), cv2.FONT_HERSHEY_SIMPLEX, .75, (50,170,50),2)

    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0XFF == 27:
        break
