import cv2 # importando o módulo cv2, que é a biblioteca OpenCV utilizada para processamento de imagens

image_path = "/home/eduarda/itan/project/black.webp"  # Insira o caminho para a imagem que vamos processar

frame = cv2.imread(image_path) # Definimos a variável image_path como a imagem que desejamos analisar

# Agora vamos passar os valores das cores de rgb para HSV, isso porque só vamos precisar dos tons laranjas 
hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 

# Obtemos as dimensões da imagem carregada usando a função shape do numpy. 
# height é a altura da imagem e width é a largura. 
# O _ é usado para ignorar o valor do canal de cores, já que não é necessário aqui.
height, width, _ = frame.shape

#Calculamos as coordenadas do pixel central da imagem, dividindo a largura por 2 para obter o centro 
# horizontal (center_x) e a altura por 2 para obter o centro vertical (center_y).

center_x = int(width / 2)
center_y = int(height / 2)

pixel_central = hsv_frame[center_y, center_x]
#Acessamos o pixel central da imagem convertida para HSV, obtendo o valor de matiz
#(hue) desse pixel. O matiz é armazenado na variável hue_value.
hue_value = pixel_central[0]

color = ""
if hue_value > 0 and hue_value <= 5:
    color += "RED"
elif hue_value > 5 and hue_value <= 22:
    color += "ORANGE"
elif hue_value > 22 and hue_value <= 33:
    color += "YELLOW"
elif hue_value > 33 and hue_value <= 78:
    color += "GREEN"
elif hue_value > 78 and hue_value <= 131:
    color += "BLUE"
elif hue_value > 131 and hue_value <= 170:
    color += "VIOLET"
elif hue_value > 170 and hue_value <= 179:
    color += "RED"
else:
    color += "indefinida"

pixel_central_bgr = frame[center_y, center_x]
b, g, r = int(pixel_central_bgr[0]), int(pixel_central_bgr[1]), int(pixel_central_bgr[2])
cv2.putText(frame, "Color: " + color, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
cv2.circle(frame, (center_x, center_y), 5, (25, 25, 25), 3)

cv2.imshow("Frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
