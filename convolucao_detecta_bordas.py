import cv2
import numpy as np


imagem_colorida = cv2.imread('static/peppers.jpg')
imagem = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

# Sobel
# Usa o filtro Sobel.
x = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=3)
y = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=3)
# Aaplica as bordas em x e y
sobel = cv2.addWeighted(x, 0.5, y, 0.5, 0)

# Roberts
# Define os kernels
kernels_x = np.array([[1, 0], [0, -1]])
kernels_y = np.array([[0, 1], [-1, 0]])
x = cv2.filter2D(imagem, -1, kernels_x)
y = cv2.filter2D(imagem, -1, kernels_y)
# Aaplica as bordas em x e y
roberts = cv2.addWeighted(x, 0.5, y, 0.5, 0)

# Prewitt
# Define os kernels
kernels_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
kernels_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
x = cv2.filter2D(imagem, -1, kernels_x)
y = cv2.filter2D(imagem, -1, kernels_y)
# Aaplica as bordas em x e y
prewitt = cv2.addWeighted(x, 0.5, y, 0.5, 0)

# Canny
# Função pronta do openvc
canny = cv2.Canny(imagem, 100, 200)

cv2.imwrite(f'results_detecta_bordas/peppers_Sobel.png', sobel)
cv2.imwrite(f'results_detecta_bordas/peppers_Roberts.png', roberts)
cv2.imwrite(f'results_detecta_bordas/peppers_Prewitt.png', prewitt)
cv2.imwrite(f'results_detecta_bordas/peppers_Canny.png', canny)
