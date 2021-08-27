import matplotlib.pyplot as plt
from PIL import Image
import cv2
import os

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

# retorna endereco relativo da pasta input
def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)


# Usando Pillow
# imagem = Image.open(in_path("LED2.jpg"))

# width, height = imagem.size
# print(width, height)

# editada = Image.open(in_path("LED2.jpg")).convert('HSV')

# usando opencv
# imag = cv2.imread(in_path("LED2.jpg"))
# cinzaImg = cv2.imread(in_path("LED2.jpg"), cv2.IMREAD_GRAYSCALE)
# height, width, channels = cinzaImg.shape  # opencv
# cv2.imshow('Original image',imag)
# cv2.imshow('pret branc image', cinzaImg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# COLOCAR PRETO EM TODOS OS PIXELS EXCETO NO LED
pilimage = Image.open(in_path("LED2.jpg"))
width, height = pilimage.size
editada = pilimage

for y in range(height):
    print('in for Y')
    for x in range(width):
        print('in for X')
        (r,g,b) = editada.getpixel((x,y))
        if not(r>=250 and g>=200 and b>=200):
            editada.putpixel((x,y), (0,0,0))
        else:
            print((r,g,b), 'pixel=', (x,y))

editada.save(in_path('editadaLED2.png'))
plt.imshow(editada)
plt.show()


# DESCOBRIR COR APROXIMADA DO LED (EM PRETO E RBANCO)
hor, vert = [], []
cor_R, cor_G, cor_B = [], [], []
imagem = Image.open(in_path("editadaLED2.png"))
for y in range(imagem.size[1]):   # height
    for x in range(imagem.size[0]):   # width
        cor=(imagem.getpixel((x,y)))
        if cor[0] >= 182 and cor[1]>=92 and cor[2]>=120:  #250,200,200
            print(cor, 'pixel=', (x,y))
            hor.append(x)
            vert.append(y)
            cor_R.append(cor[0])
            cor_G.append(cor[1])
            cor_B.append(cor[2])

print("*********** out of for *****************")
raioX = max(hor) - min(hor)
raioY = max(vert) - min(vert)
print('max horiz = ', max(hor), '#### min horiz = ', min(hor))
print('max vert = ', max(vert), '#### min vert = ', min(vert))
print('raio em X = ', raioX, ' ### raio em Y = ', raioY)

minR = min(cor_R)
minG = min(cor_G)
minB = min(cor_B)
print('minimo R,G,B = ', minR, minG, minB)

raio = raioX+raioY//2
# DEFININDO O ROI (min(hor)-max(hor), min(vert)-max(vert))
coresR, coresG, coresB = [], [], []
imagemFinal = Image.open(in_path("LED2.jpg"))
wid, hei = imagemFinal.size
for x in range(min(hor),max(hor)):
    for y in range(min(vert),max(vert)):
        coresR.append((imagemFinal.getpixel((x,y)))[0])
        coresG.append((imagemFinal.getpixel((x,y)))[1])
        coresB.append((imagemFinal.getpixel((x,y)))[2])
        imagemFinal.putpixel((x,y), (0,0,255))
        

plt.imshow(imagemFinal)
plt.show()

print('R \n', coresR, '\nmin', min(coresR))
print('G \n', coresG, '\nmin', min(coresG))
print('B \n', coresB, '\nmin', min(coresB))

