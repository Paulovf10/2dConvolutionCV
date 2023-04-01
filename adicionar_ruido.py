import cv2
import numpy as np


imagem_colorida = cv2.imread('static/peppers.jpg')
imagem = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

# Gera uma nova matriz do tamanho da imagem adicionando 100 aleatoriamente a varios pixels para gerar o ruido.
imagem_ruido = np.random.normal(0, 100, imagem.shape)

# Converte a matriz para o tipo da imagem
imagem_ruido = imagem_ruido.astype(imagem.dtype)

# Adiciona a matriz com ruido a imagem
imagem_ruido = cv2.add(imagem, imagem_ruido)


# Usa a função pronta do opencv para fazer a media à imagem com ruido retornando uma imagem parecida com a original.
imagem_filtrada = cv2.blur(imagem, (3, 3))


cv2.imwrite(f'results_adicionar_ruido/ruido-peppers.png', imagem_ruido)
cv2.imwrite(f'results_adicionar_ruido/media-peppers.png', imagem_filtrada)



