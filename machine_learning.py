import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

img = cv.inread('pokemon.jpg', 1)

img = cv.cvtColor(img.cv.COLOR_BGR2RGB)
plt.inshow(img)
plt.show

renglones, columnas, profundidad = img.shape
x = np.zeros((171720,3))
p = 0
for i in range(renglones):
  for j in range(columnas):
    x[p] = img[i,j]
    p = p+1


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 4, random_state = 0).fit(x)
print(kmeans.labels_)
kmeans.predict([[0,0,0],[255,0,0],[0,255,0],[0,0,255]])


canal = x[0:171720]
canal = canal.reshape(171720,-1)
b = kmeans.predict(canal[0:171720])

b = b.reshape(171720,-1)
c = np.zeros(171720,2)