import cv2
import imutils
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt

img1 = cv2.imread('/content/usuario_1_n.jpg')
img2 = cv2.imread('/content/usuario_2_n.jpg')
test = cv2.imread('/content/usuario_1_e.jpg')

gray_image1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

gray_image2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

gray_test = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)

histograma1 = cv2.calcHist([gray_image1], [0],None, [256], [0, 256])

histograma2 = cv2.calcHist([gray_image2], [0],None, [256], [0, 256])

histograma3 = cv2.calcHist([gray_test], [0],None, [256], [0, 256])

plt.hist(histograma1)

plt.hist(histograma2)

plt.hist(histograma3)

c1, c2 = 0, 0
   
i = 0
while i<len(histograma1) and i<len(histograma2): 
    c1+=(histograma1[i]-histograma2[i])**2
    i+= 1
c1 = c1**(1 / 2) 
   
  
i = 0
while i<len(histograma1) and i<len(histograma3): 
    c2+=(histograma1[i]-histograma3[i])**2
    i+= 1
c2 = c2**(1 / 2) 
   
if(c1<c2): 
    print("img1.jpg es mas similar que test.jpg en comparacion con img2.jpg") 
    print(c1,c2)
else: 
    print("img2.jpg es mas similar que test.jpg en comparacion con img1.jpg") 
    print(c1,c2)