import cv2
import numpy as np


imagem_colorida = cv2.imread('static/peppers.jpg')
imagem = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

# Cria a matriz do kernel com desfoque
blur_kernel = np.ones((5, 5), dtype=np.float32) / (5 * 5)

# Aplica convolução na imagem original com o kernel
imagem_desfocada = cv2.filter2D(imagem, -1, blur_kernel)


# Gera uma nova matriz do tamanho da imagem adicionando 100 aleatoriamente a varios pixels para gerar o ruido.
imagem_ruido_desfocada = np.random.normal(0, 100, imagem_desfocada.shape)

# Converte a matriz para o tipo da imagem
imagem_ruido_desfocada = imagem_ruido_desfocada.astype(imagem_desfocada.dtype)

# Adiciona a matriz com ruido a imagem com desfoque
imagem_ruido_desfocada = cv2.add(imagem_desfocada, imagem_ruido_desfocada)

# Usa o metodo Canny para detectar as bordas. (foi escolhido por ser mais simples)
bordas_imagem_desfocada = cv2.Canny(imagem_desfocada, 100, 200)
bordas_ruido_imagem_desfocada = cv2.Canny(imagem_ruido_desfocada, 100, 200)


cv2.imwrite(f'results_conv_ruido/desfocada-peppers.png', imagem_desfocada)
cv2.imwrite(f'results_conv_ruido/desfocada_ruido-peppers.png', imagem_ruido_desfocada)
cv2.imwrite(f'results_conv_ruido/bordas_desfocada-peppers.png', bordas_imagem_desfocada)
cv2.imwrite(f'results_conv_ruido/bordas_desfocada_ruido-peppers.png', bordas_ruido_imagem_desfocada)







