import cv2

img = cv2.imread("../db_aulas/Imagens/basic_shapes.png",0)
cv2.imshow("Original", img)
cv2.waitKey(0)

(_, cnts, hierarquia) = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img = cv2.imread("../db_aulas/Imagens/basic_shapes.png")
clone = img.copy()
for c in cnts:
    M = cv2.moments(c)
    cx = int(M["m10"]/M["m00"]) 
    cy = int(M["m01"]/M["m00"])
    cv2.circle(clone, (cx,cy), 10, (0, 255,0), -1)
cv2.imshow("Circle", clone)
cv2.waitKey(0)

