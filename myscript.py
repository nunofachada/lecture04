from imageio.v3 import imread
import matplotlib.pyplot as plt

img = imread('pisco.jpg')
plt.imshow(img)
plt.show()