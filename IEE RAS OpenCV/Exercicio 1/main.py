import cv2

img = cv2.imread('g retriver.jpg')

print("Altura da Imagem: ", end='')
print(img.shape[1])

print("Largura da Imagem: ", end='')
print(img.shape[0])

print("Quantidade de canais: ", end='')
print(img.shape[2])

cv2.imshow("Dogginho", img)
cv2.waitKey(0)
cv2.imwrite('dog.jpg', img)