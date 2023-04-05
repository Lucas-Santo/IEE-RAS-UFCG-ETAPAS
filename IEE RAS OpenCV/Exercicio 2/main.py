import cv2 as cv
from numpy import sin, cos, tan, sqrt

img = cv.imread('Cat.jpg')
cv.imshow("gatiu", img)

for y in range(0, img.shape[0]):
    for x in range(0, img.shape[1]):
        img[y, x] = (sin(x**2), cos(y**2), tan((x+y)**2)) # linhas verticais vermelhas
        #img[y, x] = (sqrt(x**2+2*x-6), sqrt(y**2-2*x), (x+y)) # Não sei descrever esse :v

cv.imshow("Modificado", img)

cv.waitKey(0)
cv.imwrite("Modificado.jpg", img)
