import cv2

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = camera.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    heigth, width, _ = frame.shape
    centerx = int(width / 2)
    centery = int(heigth / 2)

    pixel_central =  hsv_frame[centery, centerx]
    hue_value = pixel_central[0] 

    color = "Undefined"
    if hue_value <= 5:
        color = "RED"
    elif hue_value > 5 and hue_value <= 22:
        color = "ORANGE"
    elif hue_value > 22 and hue_value <= 33:
        color = "YELLOW"
    elif hue_value > 33 and hue_value <= 78:
        color = "GREEN"
    elif hue_value > 78 and hue_value <= 131:
        color = "BLUE" 
    elif hue_value < 170:
        color = "VIOLET"
    else:
        color = "RED"
    pixel_central_bgr = frame[centery,centerx]
    b, g, r = int(pixel_central_bgr[0]), int(pixel_central_bgr[1]), int(pixel_central_bgr[2])
    cv2.putText(frame, color, (10, 70), 0,1.5, (b,g,r), 2)
    cv2.circle(frame,(centerx, centery),5, (25,25,25), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27: ## Essa é a tecla esc
       break 
        
camera.release()        
cv2.destroyAllWindows()
