import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./Data/signature.png', 0)

kernel = np.ones((5,5), np.uint8)

img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)


plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(img_erosion, cv2.COLOR_BGR2RGB))
plt.title('Erosion')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(img_dilation, cv2.COLOR_BGR2RGB))
plt.title('Dilation')
plt.axis('off')

plt.tight_layout()
plt.show()