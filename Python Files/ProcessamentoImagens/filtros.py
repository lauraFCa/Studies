from PIL import Image, ImageFilter
from math import *
import numpy as np
from utils import *

def Filtrar():
    img = Image.open(in_path('filtros', 'cacem.jpg'))
    
    filtrada = img.filter(ImageFilter.GaussianBlur)
    filtered.save(out_path('filtros', "cacemGaussianBlur.jpg"))

    filtered1 = img.filter(ImageFilter.BLUR)
    filtered1.save(out_path('filtros', "cacemBLUR.jpg"))

    filtered2 = img.filter(ImageFilter.CONTOUR)
    filtered2.save(out_path('filtros', "cacemCONTOUR.jpg"))

    filtered3 = img.filter(ImageFilter.EMBOSS)
    filtered3.save(out_path('filtros', "cacemEMBOSS.jpg"))

    filtered4 = img.filter(ImageFilter.EDGE_ENHANCE)  # realce de arestas
    filtered4.save(out_path('filtros', "cacemEDGE.jpg"))

    filtered5 = img.filter(ImageFilter.MinFilter(7))
    """
    MinFilter(X): Pega o minimo de uma regiao da imagem - janela anda pela imagem e seleciona o menor valor de pixel dentro dessa area, e troca o pixel do meio por esse valor minimo
    """
    filtered5.save(out_path('filtros', "cacemMIN.jpg"))
    show_vertical(img, filtered)
    show_vertical(img, filtered1)
    show_vertical(img, filtered2)
    show_vertical(img, filtered3)
    show_vertical(img, filtered4)
    show_vertical(img, filtered5)


def show_box_blur(filename, r=1):
    # filtro passa baixa, para pre processamento
    original = Image.open(in_path('filtros', filename))
    filtrada = original.filter(ImageFilter.BoxBlur(r))

    show_horizontal(original, filtrada)
    outputName = '{}_boxBlur_{}.png'.format( filename[:filename.index('.')], r) #lena_boxBlur_1.png
    filterada.save(out_path('filtros', outputName ))


def show_vertical_edges(filename, offset=0):
    # Filtro de Sobel na imagem
    original = Image.open(in_path('filtros', filename)).convert('L')  # usar luminancia para converter em escala de cinza
    # Kernel = crio o filtro de Sobel ((tamanho), [lista com valores], valorDivisaoMedia, offset)
    filtrada = original.filter(ImageFilter.Kernel((3,3), [
        -1, 0, 1,
        -2, 0, 2,
        -1, 0, 1], 1, offset))

    show_horizontal(original, filtrada)
    outputName = '{}_vSobel_{}.png'.format( filename[:filename.index('.')], offset)
    filtrada.save(out_path('filtros', outputName ))


def show_edges(filename, direction='x', offset=0):
    # Filtro de Sobel na imagem
    original = Image.open(in_path('filtros', filename)).convert('L')

    Xsobel = ImageFilter.Kernel((3,3), [ # fazendo subtracoes na vertical = resultado horizontal
        -1, 0, 1,
        -2, 0, 2,
        -1, 0, 1], 1, offset)
    Ysobel = ImageFilter.Kernel((3,3), [ # fazendo subtracoes na horizontal = resultado vertical
        -1, -2, -1,
         0, 0, 0,
         1, 2, 1], 1, offset)

    if direction == 'x':
        filtrada = original.filter(Xsobel)
    elif direction == 'y':
        filtrada = original.filter(Ysobel)
    else:
        vsobel = original.filter(Xsobel)
        hsobel = original.filter(Ysobel)
        w, h = original.size
        filtrada = Image.new('L', (w,h))

        for i in range(w):
            for j in range(h):
                value = sqrt(vsobel.getpixel((i,j))**2 + hsobel.getpixel((i,j))**2)
                # value nao sera negativo de maneira nenhuma. Nao pode ser maior que 255
                value = int(min(value, 255)) #limita a 255
                filtrada.putpixel((i,j), value)

    show_horizontal(original, filtrada)
    outputName = '{}_{}Sobel_{}.png'.format( filename[:filename.index('.')], direction, offset)
    filtrada.save(out_path('filtros', outputName ))

#ERRADO
def greenmask(img):
    hsvImg = Image.open(in_path('', img)).convert('HSV')
    w, h = hsvImg.size

    hue, sat, val = [], [], []
    for x in range(w):
        for y in range(h):
            pixel = hsvImg.getpixel((x,y))
            hue.append(pixel[0])
            sat.append(pixel[1])
            val.append(pixel[2])

    channel = (np.array( [hue, sat, val] )).T
    mascara = np.ones(hsvImg.size) #crio matriz de uns, e onde identificar ser verde substituo por 0
    for i in (np.nditer(channel)):
        # for j in range(len(sat)):
        #     for k in range(len(val)):
                if 70 <= hue[i] <= 130 and sat[i] >= 50/255 and val[i]>= 50/255: 
                    #saturacao entre 0 e 1
                    mascara[i] = 0
    print(mascara)
    imagem = Image.fromarray(mascara, 'HSV')
    imagem.show()

    imagemMascara = Image.fromarray((img * mascara), 'HSV')
    imagemMascara.show()


if __name__ == "__main__":
    #Filtrar()
    #show_box_blur('lena.png', 8) # r = raio da vizinhanca
    #show_edges('death-stranding.jpg', 'a')
    (greenmask('chroma.jpg'))