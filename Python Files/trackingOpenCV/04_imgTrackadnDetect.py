import cv2

imagem = cv2.imread('imagens/pessoas.jpg')
# objetivo: colocar bounding boxes em cada pessoa da imagem
detector = cv2.CascadeClassifier('cascade/fullbody.xml') # arquivos ja treinados
imgCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow('Pessoas', imgCinza)

detections = detector.detectMultiScale(imgCinza)

print(detections,'\n',len(detections)) # posicao de cada pessoa na imagem, num de pessoas
#detections = (x, y, w, h)

for (x, y, l, a) in detections:
    cv2.rectangle(imagem, (x,y), (x+l,y+a), (0,255,0), 2)

cv2.imshow('Detections', imagem)
cv2.waitKey(0)
#cv2.destroyAllWindows()