# Introducao
# Sistema de Coordenadas e Manipulacao de Pixels
# Fatiamento e desenho sobre a imagem

import cv2

# Leitura da imagem com a função imread()
imagem = cv2.imread('stormtrooper.jpg')  # matriz numpy

''' imagem = matriz 3x3 - canais de cores R,G,B
Caso fosse em preta e branca seria 0 ou 255
Cada elemento de cor (R ou G ou B) tem um inteiro de 8 bits "uint8" '''

print('Largura em pixels: ', end='')
print(imagem.shape[1]) #largura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0]) #altura da imagem
print('Qtde de canais: ', end='')
print(imagem.shape[2])

(b, g, r) = imagem[0,0] #veja que a ordem BGR e não RGB
print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, ' Verde:', g, ' Azul:', b)

# Mostra a imagem com a função imshow
cv2.imshow("Imagem Original", imagem)
 #espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
cv2.imwrite("saida.jpg", imagem)

imagem_modificada1 = cv2.imread('stormtrooper.jpg')  # matriz numpy
# varrer a img e substituir os pixels
for y in range(0, imagem_modificada1.shape[0]): # percorre linhas
    for x in range(0, imagem_modificada1.shape[1]): # percorre colunas
        imagem_modificada1[y, x] = (255,0,0) # substitui pixel por azul
cv2.imshow("Imagem modificada 1", imagem_modificada1)


imagem_modificada2 = cv2.imread('stormtrooper.jpg')
# salto a cada 10 linhas e a cada 10 colunas
for y in range(0, imagem_modificada2.shape[0], 10): # percorre linhas de 10 em 10
    for x in range(0, imagem_modificada2.shape[1], 10): # percorre colunas de 10 em 10
        imagem_modificada2[y:y+5, x: x+5] = (0,255,255) # cria quadrado 5x5
cv2.imshow("Imagem modificada 2", imagem_modificada2) 


# Slicing 
vermelho = (0, 0, 255)
verde = (0, 255, 0)
azul = (255, 0, 0)
img = cv2.imread('stormtrooper.jpg')

# slicing - alterar varios pixels de uma vez
img[30:50, :] = vermelho  # Cria um retangulo vermelho por toda a largura da imagem
img[100:150, 50:100] = (0, 0, 255)  # Cria um quadrado vermelho 
img[:, 200:220] = (0, 255, 255)  # Cria um retangulo amarelo por toda a altura da imagem
img[150:300, 250:350] = (0, 255, 0)  # Cria um retangulo verde da linha 150 a 300 nas colunas 250 a 350
img[300:400, 50:150] = (255, 255, 0)  # Cria um quadrado ciano da linha 150 a 300 nas colunas 250 a 350
img[250:350, 300:400] = (255, 255, 255)  # Cria um quadrado branco
img[70:100, 300: 450] = (0, 0, 0)  # Cria um quadrado preto
cv2.imshow("Imagem alterada", img)
cv2.imwrite("alterada.jpg", img) 

# Utilizando funcoes do OpenCV
cv2.line(imagem, (0, 0), (100, 200), verde)
cv2.line(imagem, (300, 200), (150, 150), vermelho, 5)
cv2.rectangle(imagem, (20, 20), (120, 120), azul, 10)
cv2.rectangle(imagem, (200, 50), (225, 125), verde, -1)
(X, Y) = (imagem.shape[1] // 2, imagem.shape[0] // 2) 
for raio in range(0, 175, 15): 
    cv2.circle(imagem, (X, Y), raio, vermelho)
#escrever texto na imagem
fonte = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagem,'OpenCV',(15,65), fonte, 2,(255,255,255),2,cv2.LINE_AA)

cv2.imshow("Desenhando sobre a imagem", imagem)
cv2.waitKey(0)