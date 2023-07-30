import cv2

img = cv2.imread("/home/eduarda/itan/project/orange_fruit.webp")
cv2.imshow("img", img)
cv2.waitKey(0)

print(img)


# Se fosse uma inteiramente azul  a matriz retornada seria  [154,0,1] B G R 
