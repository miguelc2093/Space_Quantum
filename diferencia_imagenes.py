import cv2
import imutils

imagen1 = cv2.imread('/content/usuario_1_e.jpg')
imagen2 = cv2.imread('/content/usuario_2_e.jpg')

from google.colab.patches import cv2_imshow
cv2_imshow(imagen2)

imagen1.shape

imagen2.shape

new1 = cv2.resize(imagen1, (450,600))
cv2_imshow(new1)

new2 = cv2.resize(imagen2, (450,600))
cv2_imshow(new2)

diferencia = cv2.absdiff(new1,new2)
Conv_hsv_Gray = cv2.cvtColor(diferencia, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255,cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)
diferencia[mask != 255] = [0, 0, 255]

cv2.imwrite('/content/diferencia.jpg',diferencia)

cv2_imshow(diferencia)

