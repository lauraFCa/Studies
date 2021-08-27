from PIL import Image
from utils import *


def greyScale(colored):
    w, h = colored.size
    img = Image.new("RGB", (w,h))

    for x in range(w):
        for y in range(h):
            pixel = colored.getpixel((x,y))
            luminancia = (pixel[0]+pixel[1]+pixel[2])//3 #media dos valores RGB
            img.putpixel((x,y), (luminancia, luminancia, luminancia))
    return img


def ponderadaGreyScale(colored):
    w, h = colored.size
    img = Image.new("RGB", (w,h))

    for x in range(w):
        for y in range(h):
            pixel = colored.getpixel((x,y))
            luminancia = int(0.3*pixel[0] + 0.59*pixel[1] + 0.11*pixel[2]) #media ponderada dos valores RGB
            img.putpixel((x,y), (luminancia, luminancia, luminancia))
    return img



if __name__ == "__main__":
    img = Image.open(in_path("puppy_bw.jpg"))
    print(img.getpixel((100,100)))
    print(img.getpixel((1000,1000)))
    print(img.getpixel((500,500)))

    puppy = Image.open(in_path("puppy.jpg"))
    pb_puppy = ponderadaGreyScale(puppy) # ponderada fiocu mais clara
    pb_puppy.save(out_path("pb_ponderada_puppy.jpg"))