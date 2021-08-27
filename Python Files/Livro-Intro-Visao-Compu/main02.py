# Transformações e mascaras
# Sistemas de Cores

import cv2
import numpy as np

imagem = cv2.imread('puppy.jpg')
# cortar imagem
recorte = imagem[450:900, 1100:1700]  # 450 a 900px na vertical // 1100 a 1700px na horizontal
cv2.imshow("Recorte da imagem", recorte)
cv2.imwrite("recorte.jpg", recorte) #salva no disco

#redimensionar
cv2.imshow("Original", imagem) 
largura = imagem.shape[1] 
altura = imagem.shape[0] 
proporcao = float(altura/largura)  # evitar distorcao na img
largura_nova = 320 #em pixels 
altura_nova = int(largura_nova*proporcao)
tamanho_novo = (largura_nova, altura_nova)
img_redimensionada = cv2.resize(imagem, tamanho_novo, interpolation = cv2.INTER_AREA)
cv2.imshow('Resultado', img_redimensionada) 

# redimensionar com slicing
"""refaz a imagem interpolando linhas e colunas, ou seja, pega a primeira linha, 
ignora a segunda, depois pega a terceira linha, ignora a quarta, e assim por 
diante. O mesmo é feito com as colunas"""
img_redimensionada2 = imagem[::2,::2] # vai de 2 em 2
cv2.imshow("Redimensionada com Interpolacao", img_redimensionada)

cv2.waitKey()
cv2.destroyAllWindows()

# espelhar
img = cv2.imread('saida.jpg') 
cv2.imshow("Original", img) 
flip_horizontal = img[::-1,:] #comando equivalente abaixo
#flip_horizontal = cv2.flip(img, 1)
cv2.imshow("Flip Horizontal", flip_horizontal) 
flip_vertical = img[:,::-1] #comando equivalente abaixo 
#flip_vertical = cv2.flip(img, 0)
cv2.imshow("Flip Vertical", flip_vertical) 
flip_hv = img[::-1,::-1] #comando equivalente abaixo
#flip_hv = cv2.flip(img, -1) 
cv2.imshow("Flip Horizontal e Vertical", flip_hv)

# rotacionar
img1 = cv2.imread('recorte.jpg')
(alt, lar) = img1.shape[:2] #captura altura e largura 
print('altura e largura: ', img1.shape[:2])
centro = (lar//2, alt//2) #acha o centro 
M = cv2.getRotationMatrix2D(centro, 30, 1.0) #30 graus 
img_rotacionada = cv2.warpAffine(img1, M, (lar, alt))
cv2.imshow("Imagem rotacionada em 45 graus", img_rotacionada)

cv2.waitKey()
cv2.destroyAllWindows()

# Mascaras
imagem1 = cv2.imread('stormtrooper.jpg')
cv2.imshow("Original", imagem1) 

mascara = np.zeros(imagem1.shape[:2], dtype = "uint8") 
(cX, cY) = (imagem1.shape[1] // 2, imagem1.shape[0] // 2) 
# cv2.circle(mascara, (cX, cY), 100, 255, -1) 
cv2.circle(mascara, (cX, cY), 180, 255, 70)
cv2.circle(mascara, (cX, cY), 70, 255, -1)
img_com_mascara = cv2.bitwise_and(imagem1, imagem1, mask = mascara) 
cv2.imshow('Mascara', mascara)
cv2.imshow("Mascara aplicada a imagem", img_com_mascara) 

cv2.waitKey()
cv2.destroyAllWindows()

# Cores
imagem2 = cv2.imread('cores.jpg')
cv2.imshow("Original", imagem2)
gray = cv2.cvtColor(imagem2, cv2.COLOR_BGR2GRAY) 
cv2.imshow("Gray", gray) 
hsv = cv2.cvtColor(imagem2, cv2.COLOR_BGR2HSV) 
cv2.imshow("HSV", hsv)
lab = cv2.cvtColor(imagem2, cv2.COLOR_BGR2LAB) 
cv2.imshow("L*a*b*", lab) 

# separar canais de uma img
imagem2 = cv2.imread('cores.jpg')
(canalAzul, canalVerde, canalVermelho) = cv2.split(imagem2) 
cv2.imshow("Vermelho", canalVermelho) 
cv2.imshow("Verde", canalVerde) 
cv2.imshow("Azul", canalAzul) 

# alterar os np array de cada canal
resultado = cv2.merge([canalAzul, canalVerde, canalVermelho])
cv2.imshow('Juntar canais', resultado)

cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow("Original", imagem2)
zeros = np.zeros(imagem2.shape[:2], dtype = "uint8")
cv2.imshow("Vermelho", cv2.merge([zeros, zeros, canalVermelho]))
cv2.imshow("Verde", cv2.merge([zeros, canalVerde, zeros])) 
cv2.imshow("Azul", cv2.merge([canalAzul, zeros, zeros])) 
cv2.imshow("Original", imagem2)


cv2.waitKey()
cv2.destroyAllWindows()
