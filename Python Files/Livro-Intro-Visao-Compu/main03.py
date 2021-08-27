# Histogramas e equalizacao de imagem

import cv2
import numpy as np
from matplotlib import pyplot as plt

original = cv2.imread('estrada.jpg') 
img = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY) # converte P&B 
cv2.imshow('original', original)
cv2.imshow("Imagem P&B", img)
h = cv2.calcHist([img], [0], None, [256], [0, 256])  #Funcao calcHist para calcular o histograma da imagem
plt.figure() 
plt.title("Histograma P&B") 
plt.xlabel("Intensidade") 
plt.ylabel("Qtde de Pixels") 
plt.plot(h, label='Histograma') 
# plt.hist(img.ravel(),256,[0,256], label="histograma ate 300")  # ravel = eixo x vai ateh 300 (passando valor de 255 - onde nao ha pixels)
plt.xlim([0, 256]) 
plt.legend()
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

# Histograma de img colorida
original = cv2.imread('estrada.jpg') 
cv2.imshow('original', original)
#Separa os canais
canais = cv2.split(original) 
cores = ("b", "g", "r") 
plt.figure() 
plt.title("Histograma Colorido") 
plt.xlabel("Intensidade") 
plt.ylabel("Número de Pixels") 
for (canal, cor) in zip(canais, cores): 
    print(canal, cor)
    #Este loop executa 3 vezes, uma para cada canal 
    hist = cv2.calcHist([canal], [0], None, [256], [0, 256]) 
    plt.plot(hist, cor) 
    plt.xlim([0, 256]) 
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()

# Equalizando histograma
img = cv2.imread('estrada.jpg') 
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h_eq = cv2.equalizeHist(img)
plt.figure() 
plt.title("Histograma Equalizado vs Original") 
plt.xlabel("Intensidade") 
plt.ylabel("Qtde de Pixels") 
plt.hist(h_eq.ravel(), 256, [0,256], label='Equalizado') 
plt.hist(img.ravel(), 256, [0,256], label='Original') 
plt.legend()
plt.xlim([0, 256]) 

cv2.imshow('original', img)
cv2.imshow('equalizada', h_eq)

cv2.waitKey()
cv2.destroyAllWindows()
