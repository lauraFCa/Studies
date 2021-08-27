import cv2
import numpy as np

cap = cv2.VideoCapture("videos/race.mp4")
ret, first_frame = cap.read()
frame_gray_init = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

hsv = np.zeros_like(first_frame)

hsv[..., 1] # definir saturacao (primeiro canal) para o maximo

while True:
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    flow = cv2.calcOpticalFlowFarneback(frame_gray_init, frame_gray, None,0.5, 3, 15, 3,5,1.2,0)
    magnitude, angle = cv2.cartToPolar(flow[...,0], flow[...,1])
    # definir distancia da imagem
    hsv[...,0] = angle*(180/(np.pi/2)) # matiz - convertendo angulo
    hsv[...,2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX) # atualizar value - cor
    final = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow('Dense Optical Flow', final)
    if cv2.waitKey(1) == 13:
        break

    frame_gray_init = frame_gray

cap.release()
cv2.destroyAllWindows()