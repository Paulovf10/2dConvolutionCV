import cv2
import numpy as np


imagem_colorida = cv2.imread('static/Lenna.png')
imagem = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)
while True:
    kernel = int(input("Escolha a escala do kernel entre 3, 5, 7 ou 9: "))
    if kernel == 0:
        break
    elif kernel not in [3, 5, 7, 9]:
        print("Apenas as opções 3, 5, 7 ou 9 estão disponiveis.")
    else:
        # Adiciona o padding as imagens.
        imagem_pad = np.pad(imagem, ((kernel // 2, kernel // 2), (kernel // 2, kernel // 2)), mode='constant')
        # Cria uma matriz zerada para ser nossa proxima imagem.
        imagem_conv = np.zeros(imagem.shape, dtype=np.float32)
        # Cria uma matriz de 1 normalizada.
        kernel_matiz = np.ones((kernel, kernel), dtype=np.float32) / (kernel ** 2)
        # Entra em cada pixel da imagem.
        for i in range(imagem.shape[0]):
            for j in range(imagem.shape[1]):
                # Aplica a convolução em cada pixel.
                imagem_conv[i, j] = np.sum(imagem_pad[i:i + kernel, j:j + kernel] * kernel_matiz)
        cv2.imwrite(f'results_media_movel/Lenna_{kernel}x{kernel}-media_movel.png', imagem_conv)
        print("OBS: Digite 0 caso queria encerar o programa")

