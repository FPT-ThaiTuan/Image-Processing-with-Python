import cv2
from matplotlib import pyplot as plt

imgA = cv2.cvtColor(cv2.imread("./Data/BorderImage.jpg"), cv2.COLOR_BGR2RGB)
imgB = cv2.cvtColor(cv2.imread("./Data/Image.jpg"), cv2.COLOR_BGR2RGB)

imgA = cv2.resize(imgA, (500, 500))
imgB = cv2.resize(imgB, (500, 500))

final_img = cv2.addWeighted(imgA, 0.2, imgB, 0.8, 0)

plt.subplot(1, 3, 1)
plt.imshow(imgA)
plt.axis("off")
plt.title('Image A')

plt.subplot(1, 3, 2)
plt.imshow(imgB)
plt.axis("off")
plt.title('Image B')

plt.subplot(1, 3, 3)
plt.imshow(final_img)
plt.axis("off")
plt.title('Final Image')

plt.show()
