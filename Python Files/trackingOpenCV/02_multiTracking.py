import cv2
import sys
from random import randint

print(cv2.__version__)
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']

def createTracker(trackerType):
    if trackerType == tracker_types[0]:
        tracker = cv2.TrackerBoosting_create()
    elif trackerType == tracker_types[1]:
        tracker = cv2.TrackerMIL_create()
    elif trackerType == tracker_types[2]:
        tracker = cv2.TrackerKCF_create()
    elif trackerType == tracker_types[3]:
        tracker = cv2.TrackerTLD_create()
    elif trackerType == tracker_types[4]:
        tracker = cv2.TrackerMedianFlow_create()
    elif trackerType == tracker_types[5]:
        tracker = cv2.TrackerMOSSE_create()
    elif trackerType == tracker_types[6]:
        tracker = cv2.TrackerCSRT_create()
    else:
        tracker = None
        print('Nome incorreto\nOs rastreadores disponiveis sao:')
        print(tracker_types)

    return tracker


cap = cv2.VideoCapture('videos/race.mp4')
ok, frame = cap.read() # leitura do primeiro frame do video
if not ok:
    print('Nao e possivel ler o arquivo de video')
    sys.exit(1)

bboxes = [] # lista com bounding boxes
colors = [] # lista para as cores

while True:
    # loop para o primeiro frame = guardar os bboxes e as cores
    bbox = cv2.selectROI('Multitracking', frame, False)
    bboxes.append(bbox)
    colors.append( (randint(0,255), randint(0,255), randint(0,255)) )
    print('Pressione qualquer tecla para selecionar o proximo objeto')
    print('Pressione Q para sair das caixas de selecao e comecar a rastrear')
    k=cv2.waitKey(0)
    if k==ord('q'):
        break

print('Caixas selecionadas: {0}'.format(bboxes))

multitracker = cv2.MultiTracker_create()
for bbox in bboxes:
    multitracker.add(createTracker('CSRT'), frame, bbox) # inicializar algoritmos

while cap.isOpened():
    ok, frame = cap.read()
    if not ok:
        break
    
    ok, boxes = multitracker.update(frame)
    for i, newBox in enumerate(boxes):
        (x, y, w, h) = [int(v) for v in newBox]
        cv2.rectangle(frame, (x,y), (x+w, y+h), colors[i], 2,1)

    cv2.imshow('Multitracker', frame)
    k=cv2.waitKey(1)
    if k == ord('Q'):
        break