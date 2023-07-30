import cv2
import numpy as np


def change_color(image_path, red_level, green_level, blue_level):
    # Carregar a imagem
    image = cv2.imread(image_path)

    # Definir os níveis de vermelho, verde e azul
    red = int(red_level)
    green = int(green_level)
    blue = int(blue_level)

    # Criar uma matriz de cores a ser adicionada à imagem
    color_matrix = np.full(image.shape, (blue, green, red), dtype=np.uint8)

    # Adicionar a matriz de cores à imagem original
    new_image = cv2.add(image, color_matrix)

    # Exibir a imagem original e a imagem com a cor alterada
    cv2.imshow('Imagem Original', image)
    cv2.imshow('Imagem com Cor Alterada', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Caminho da imagem
image_path = 'caminho/para/imagem.jpg'

# Pedir os níveis de vermelho, verde e azul ao usuário
red_level = input('Digite o nível de vermelho (0-255): ')
green_level = input('Digite o nível de verde (0-255): ')
blue_level = input('Digite o nível de azul (0-255): ')

# Chamar a função para alterar a cor da imagem
change_color(image_path, red_level, green_level, blue_level)
