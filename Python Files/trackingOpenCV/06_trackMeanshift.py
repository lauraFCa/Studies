import cv2, time
from imutils.video import VideoStream

# Meanshift - baseado em cores (Funciona melhor no HSV)
cap = VideoStream(src=0).start()
time.sleep(1.0) # atraso na inicializacao da webcam - para adaptacao da cam ao ambiente

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

bbox = cv2.selectROI(frame, False)
x, y, w, h = bbox
track_window = (x, y, w, h)

roi = frame[y:y+h, x:x+w] #parte dentro do bbox
cv2.imshow('ROI', roi)
# cv2.waitKey(0)

# CONVERTER BGR em HSV
hsvROI = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
cv2.imshow('ROI HSV', hsvROI)
# cv2.waitKey(0)

roi_hist = cv2.calcHist([hsvROI], [0], None, [180], [0,180]) # imagem, numero de canais, mascara, tamanho do histograma, faixa das tonalidades
"""OLHANDO O HISTOGRAMA"""
# import matplotlib.pyplot as plt
# plt.hist(roi.ravel(), 180, [0,180])
# plt.show()
# cv2.waitKey(0)

roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX) # normalizar 0 a 1
# histograma tem valor de 0 a 255 - normalizamos para 0 a 1

term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1) # criterios de parada
# EPS = quantidade de repeticoes (maior repeticao, maior precisao, menor velocidade) para encontrar o ponto com maior densidade
# COUNT = y -mais sensivel a mudancas no pixels (maior sensibilidade, maior precisao na deteccao mas nao lida bem com variacoes bruscas)

while True:
    ret, frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1) # calculo que leva ao ponto de maior densidade
        # essa funcao vai computar a probabilidade de cada elemento relacionado com a distribuicao de probabilidade
        ret, track_window = cv2.meanShift(dst, (x, y, w, h), term_crit)

        x, y, w, h = track_window
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

        cv2.imshow('Meanshift Tracking', frame)
        cv2.imshow('dst', dst)
        cv2.imshow('ROI', roi)

        if cv2.waitKey(1) == 13: #enter
            break

    else:
        break


cv2.destroyAllWindows()
cap.release()