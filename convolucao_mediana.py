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
        imagem_pad = cv2.copyMakeBorder(imagem, kernel // 2, kernel // 2, kernel // 2, kernel // 2, cv2.BORDER_REPLICATE)
        # Cria uma matriz zerada para ser nossa proxima imagem.
        imagem_conv = np.zeros_like(imagem)
        # Pega a largura e a altura da imagem
        altura, largura = imagem.shape
        # Entra em cada pixel da imagem.
        for y in range(altura ):
            for x in range(largura):
                # Aplica a convolução em cada pixel.
                window = imagem_pad[y:y + kernel, x:x + kernel]
                imagem_conv[y, x] = np.median(window)
        cv2.imwrite(f'results_mediana/Lenna_{kernel}x{kernel}-mediana.png', imagem_conv)
        print("OBS: Digite 0 caso queria encerar o programa")

