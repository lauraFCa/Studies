from PIL import Image
import os
import numpy as np # mostrar 2 imagens juntas

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

def in_path(dir, filename):
    return os.path.join(INPUT_FOLDER, dir, filename)


def out_path(dir, filename):
    return os.path.join(OUTPUT_FOLDER, dir, filename)


def show_vertical(img1, img2):
    im = Image.fromarray(np.vstack((np.array(img1), np.array(img2))))
    im.show()
    return im


def show_horizontal(img1, img2):
    im = Image.fromarray(np.hstack((np.array(img1), np.array(img2))))
    im.show()
    return im