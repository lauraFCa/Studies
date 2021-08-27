import cv2
import numpy as np

cap = cv2.VideoCapture('trackingOpenCV\\videos\\LED.mp4')
#cap = cv2.VideoCapture('LED.mp4')
# criar elemento em formato de elipse
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3)) # elemento estruturante p/ ajudar na deteccao
# subtracao do fundo da img
#fgbg = cv2.createBackgroundSubtractorKNN()

"""
createBackgroundSubtractorKNN
Essa funcao itera atraves de cada frame do video e transforma o primeiro plano com o fundo, 
ajudando assim o foco a ficar apenas no objeto que precisa ser rastreado entre os frames. 
O algoritmo K-vizinho mais proximo (KNN) classifica os pontos de dados desconhecidos encontrando
a classe mais comum entre os exemplos “k” mais proximos. 
Cada ponto de dados nos k exemplos mais proximos aumenta o peso, e o unico peso maximo e usado 
para classificar o objeto.
"""

# detectar obj em movimento e marcar com caixa delimitadora
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #converter para HSV

    cor_led_min = np.array([115,120,200]) # B  G  R   115,110,210
    cor_led_max = np.array([255,255,255]) 
    color_mask = cv2.inRange(hsv, cor_led_min, cor_led_max) #Verifica se os elementos da matriz estão entre os elementos de duas outras matrizes    
    
    (couts,hir) = cv2.findContours(color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cout in couts:
        area = cv2.contourArea(cout)
        # se a forma contornada tiver area maior que 200 considero obj de interesse
        if (area > 300 and area < 600):
            x,y,w,h = cv2.boundingRect(cout)
            frame = cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0), 2)
    cv2.imshow('Window', frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
         break

cap.realese()
cv2.destroyAllWindows()