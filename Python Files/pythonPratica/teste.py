from PIL import Image

infile = 'puppy.jpg'
outfile = 'puppyVirado.jpg'

imagem = Image.open(infile)
imagem.rotate(90).save(outfile)