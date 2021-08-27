import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('estrada.jpg')
img = img[::2,::2] # Diminui a imagem

# Suavização de imagens
suaveBlur = np.vstack([np.hstack([img, cv2.blur(img, (3, 3))]), np.hstack([cv2.blur(img, (5,5)), cv2.blur(img, (7,7))]), np.hstack([cv2.blur(img, (9,9)), cv2.blur(img, (11, 11))])])
"""
np.hstack([ img, cv2.blur( img, (3, 3) ) ]),
np.hstack([ cv2.blur(img, (5,5)), cv2.blur(img, ( 7, 7))]), 
np.hstack([ cv2.blur(img, (9,9)), cv2.blur(img, (11, 11)) ])
"""
cv2.imshow("Imagens suavisadas (Blur)", suaveBlur)

suaveGaussiano = np.vstack([np.hstack([img,cv2.GaussianBlur(img, ( 3, 3), 0)]),np.hstack([cv2.GaussianBlur(img, ( 5, 5), 0),cv2.GaussianBlur(img, ( 7, 7), 0)]),np.hstack([cv2.GaussianBlur(img, ( 9, 9), 0),cv2.GaussianBlur(img, (11, 11), 0)])])
"""
np.hstack([ img,cv2.GaussianBlur(img, (3, 3), 0) ]),
np.hstack([ cv2.GaussianBlur(img, (5, 5), 0),cv2.GaussianBlur(img, ( 7, 7), 0) ]),
np.hstack([ cv2.GaussianBlur(img, (9, 9), 0),cv2.GaussianBlur(img, (11, 11), 0) ])
"""
cv2.imshow("Imagem original e suavisadas pelo filtro Gaussiano", suaveGaussiano)

suaveMedian = np.vstack([np.hstack([img,cv2.medianBlur(img, 3)]),np.hstack([cv2.medianBlur(img, 5),cv2.medianBlur(img, 7)]),np.hstack([cv2.medianBlur(img, 9),cv2.medianBlur(img, 11)])])
"""
np.hstack([ img,cv2.medianBlur(img, 3) ]),
np.hstack([ cv2.medianBlur(img, 5), cv2.medianBlur(img, 7) ]),
np.hstack([ cv2.medianBlur(img, 9), cv2.medianBlur(img, 11) ])
"""
cv2.imshow("Imagem original e suavisadas pela mediana", suaveMedian)

suaveBiLat = np.vstack([np.hstack([img,cv2.bilateralFilter(img, 3, 21, 21)]), np.hstack([cv2.bilateralFilter(img, 5, 35, 35), cv2.bilateralFilter(img, 7, 49, 49)]), np.hstack([cv2.bilateralFilter(img, 9, 63, 63), cv2.bilateralFilter(img, 11, 77, 77)])])
"""
np.hstack([ img,cv2.bilateralFilter(img, 3, 21, 21) ]), 
np.hstack([ cv2.bilateralFilter(img, 5, 35, 35), cv2.bilateralFilter(img, 7, 49, 49) ]), 
np.hstack([ cv2.bilateralFilter(img, 9, 63, 63), cv2.bilateralFilter(img, 11, 77, 77) ])
"""
cv2.imshow("Imagem original e suavisadas pelo filtro Bilateral", suaveBiLat)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Binarização com limiar
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
suave = cv2.GaussianBlur(img, (7, 7), 0) # aplica blur 
(T, bin) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY)
(T, binI) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY_INV)
resultado = np.vstack([np.hstack([suave, bin]), np.hstack([binI, cv2.bitwise_and(img, img, mask = binI)])])
"""
np.hstack([suave, bin]),
np.hstack([binI, cv2.bitwise_and(img, img, mask = binI)])
"""
cv2.imshow("Binarizacao da imagem", resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()