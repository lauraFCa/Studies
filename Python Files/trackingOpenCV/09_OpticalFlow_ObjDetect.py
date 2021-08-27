import cv2
import numpy as np

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
cinzaInicial = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
parameters_lucasKanade = dict(winSize = (15, 15), maxLevel = 4, 
    criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)) # piramides

def selectPoint(event, x, y, flags, params):
    global point, pointSelected, old_points #pontos, se usario selecionou pontos, posicao antiga
    if event == cv2.EVENT_LBUTTONDOWN: #botao esquerdo do mouse
        point = (x, y)
        pointSelected = True
        old_points = np.array([ [x,y] ], dtype=np.float32) # matriz, tipo de dados


cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', selectPoint) # associar a funcao a janela do opencv

pointSelected, point, old_points = False, (), np.array([[]])
mask = np.zeros_like(frame)

while True:
    ret, frame = cap.read()
    frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if pointSelected is True:
        cv2.circle(frame, point, 5, (0,0,255),2)
        new_points, status, erros = cv2.calcOpticalFlowPyrLK(cinzaInicial, frameCinza, old_points, None, **parameters_lucasKanade) #algoritmo do R

        cinzaInicial = frameCinza.copy()
        old_points = new_points

        x,y = new_points.ravel()
        j,k = old_points.ravel()

        mask = cv2.line(mask, (x,y), (j,k), (0,255,255), 2)
        frame = cv2.circle(frame, (x,y), 5, (0,255,0), -1)
    
    img = cv2.add(frame, mask)
    # cv2.imshow('OpticalFlow Sparce', img)
    cv2.imshow('Frame', frame)
    cv2.imshow('Frame Mascara', mask)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()