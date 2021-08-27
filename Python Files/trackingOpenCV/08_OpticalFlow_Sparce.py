import cv2
import numpy as np

# SPARCE
cap = cv2.VideoCapture('videos/walking.avi')
# detecta cantos iniciais no primeiro frame da img

parameters_shiTomasi = dict(maxCorners=100, qualityLevel=0.3, minDistance=7) # pontos iniciais
# maxCorners = Maximo de cantos retornados (no frame inicial)
# qualityLevel = Qualidade minima para os cantos - cada canto encontrado vai ter um valor de qualidade, o com a melhor nota usa para avaliar os outros
# minDistance = menor distancia entre cantos - para considerar objetos diferentes (7 padrao da documentacao)

parameters_lucasKanade = dict(winSize=(15, 15), maxLevel=2, 
    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)) # piramides
# winSize = redimensionamento em pixels
# maxLevel = niveis da piramide (mais niveis, mais lento)
# criteria = criterio de parada do algoritmo (numero de repeticoes ou sensibilidade dos pixels)

colors = np.random.randint(0, 255, (100, 3)) # cada canto tera uma cor (100), R G B (3)

ret, frame = cap.read()
cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cantos = cv2.goodFeaturesToTrack(cinza, mask=None, **parameters_shiTomasi) # os cantos retornados

mask = np.zeros_like(frame) # mascara com mesmas dimensoes do frame, para melhor visualizacao
print(np.shape(mask))

while True:
    ret, frame = cap.read()
    frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detecta apenas os cantos retornados
    novosCantos, status, erros = cv2.calcOpticalFlowPyrLK(cinza, frameCinza, cantos, None, **parameters_lucasKanade) #algoritmo do R

    novos = novosCantos[status==1] #armazeno onde status=1, rastreaveis
    antigos = cantos[status==1]

    for i, (new, old) in enumerate(zip(novos, antigos)):
        a, b = new.ravel()
        c, d = old.ravel()

        mask = cv2.line(mask, (a,b), (c,d), colors[i].tolist(), 2)

        frame = cv2.circle(frame, (a,b), 5, colors[i].tolist(), -1)
    
    img = cv2.add(frame, mask)
    cv2.imshow('OpticalFlow Sparce', img)
    if cv2.waitKey(1)==13:
        break

    cinza = frameCinza.copy()
    cantos = novos.reshape(-1,1,2)

cv2.destroyAllWindows()
cap.release()