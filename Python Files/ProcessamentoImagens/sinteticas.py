#imagens criadas na mao
from PIL import Image
import os

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED_FRANCA = (239, 65, 53)
BLUE = (0, 85, 164)
RED_JAPAN = (173, 35, 51)
GREEN = (0, 156, 59)
YELLOW = (255, 223, 0)
BLUE_BRASIL = (0, 39, 118)

#retorna endereco relativo da pasta input
def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)


def triangulo(size): # criar imagem divida ao "meio"    
    imagem = Image.new("RGB", (size,size), WHITE)

    for x in range(size):
        for y in range(size):
            if x < y:
                imagem.putpixel((x,y), BLACK)

    return imagem


def bandeiraFranca(height):
    width = height * 3//2 # divisao inteira
    imagem = Image.new("RGB", (width,height), WHITE)

    offset = width//3  # proporcao de cada cor e a mesma (1/3 azul, 1/3 branco, 1/3 red)
    for x in range(offset):
        for y in range(height):
            imagem.putpixel((x,y), BLUE)
            imagem.putpixel((x+2*offset, y), RED_FRANCA) # red posso pintar pegando intervalo apos azul e branco
    return imagem


def bandeiraJapao(height):
    # circulo ocupa 3/5 da altura, centralizado
    width = height * 3//2
    raio = int((3*height/5)/2)
    #raio = 3*height//2
    center = (width//2, height//2)

    imagem = Image.new("RGB", (width, height), WHITE)

    #calcular coordenadas do quadrado em torno do circulo
    for x in range(center[0]-raio, center[0]+raio):
        for y in range(center[1]-raio, center[1]+raio):
            if (x - center[0])**2 + (y - center[1])**2 <= raio**2: # x^2 + y^2 = r^2
                imagem.putpixel((x,y), RED_JAPAN)

    return imagem


def bandeiraBrasil(height):
    width = (height*20//14)
    center = (width//2, height//2)
    
    imagem = Image.new("RGB", (width,height), GREEN)
    
    proporcao = int((height*1.7/20))  # distancia das pontas losango a borda 
    raio = int(width*3.5/20)

    # LOSANGO - Dividir em quatro quadrantes (esquerda -> direita, cima -> baixo)
    # quadrante 1
    for Xq1 in range(proporcao, center[0]):
        aq1 = (center[1]-proporcao)/(proporcao-center[0])
        bq1 = center[1] - proporcao*aq1
        for Yq1 in range(proporcao, center[1]):
            if Yq1 > (aq1*Xq1 + bq1):
                imagem.putpixel((Xq1,Yq1), YELLOW)

    # quadrante 2
    for Xq2 in range(center[0], (width-proporcao)):
        aq2 = (center[1]-proporcao)/(width-proporcao-center[0])
        bq2 = proporcao-center[0]*aq2
        for Yq2 in range(proporcao, center[1]):
            if Yq2 > (aq2*Xq2 + bq2):
                imagem.putpixel((Xq2,Yq2), YELLOW)

    # quadrante 3
    for Xq3 in range(proporcao, center[0]):
        for Yq3 in range(center[1], (height-proporcao)):
            aq3 = (height-proporcao-center[1])/(center[0]-proporcao)
            bq3 = center[1]-aq3*proporcao
            if Yq3 < (aq3*Xq3 + bq3):
                imagem.putpixel((Xq3,Yq3), YELLOW)

    # quadrante 4
    for Xq4 in range(center[0], (width-proporcao)):
        for Yq4 in range(center[1], (height-proporcao)):
            aq4 = (center[1]-height+proporcao)/(width-proporcao-center[0])
            bq4 = height-proporcao-aq4*center[0]
            if Yq4 < (aq4*Xq4 + bq4):
                imagem.putpixel((Xq4,Yq4), YELLOW)

    # circulo
    for xC in range((center[0]-raio), (center[0]+raio)):
        for yC in range((center[1]-raio), (center[1]+raio)):
            if (xC - center[0])**2 + (yC - center[1])**2 <= raio**2: # x^2 + y^2 = r^2
                imagem.putpixel((xC,yC), BLUE_BRASIL)

    return imagem


if __name__ == "__main__":
    brasil = bandeiraBrasil(800)
    brasil.save(os.path.join(OUTPUT_FOLDER, "bandeira_brasil.jpg"))
    brasil.show()

    t = triangulo(800)
    t.save(os.path.join(OUTPUT_FOLDER, "triangulo.jpg"))
    t.show()

    bandeira = bandeiraFranca(800)
    bandeira.save(os.path.join(OUTPUT_FOLDER, "bandeira_franca.jpg"))
    bandeira.show()
    
    bandeiraJ = bandeiraJapao(800)
    bandeiraJ.save(os.path.join(OUTPUT_FOLDER, "bandeira_japao.jpg"))
    bandeiraJ.show()
    
    print("Imagem salvas na pasta {}".format(OUTPUT_FOLDER))
