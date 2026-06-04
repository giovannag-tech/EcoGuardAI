import cv2
import numpy as np

imagem = cv2.imread("visao_computacional/folha.jpg")

hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

verde_baixo = np.array([35, 50, 50])
verde_alto = np.array([85, 255, 255])

mascara = cv2.inRange(hsv, verde_baixo, verde_alto)

porcentagem_verde = (
    np.count_nonzero(mascara)
    / mascara.size
) * 100

print(f"Área verde: {porcentagem_verde:.2f}%")

if porcentagem_verde > 30:
    print("PLANTA SAUDÁVEL")
else:
    print("ALERTA DE DOENÇA")