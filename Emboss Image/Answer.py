import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
img = cv2.imread('./Data/test.jpg')

# Different kernels can be changed to highlight image features

# Create an embossing kernel
kernel_emboss_1 = np.array([[-2, -1, 0],
                             [-1,  1, 1],
                             [ 0,  1, 2]])

kernel_emboss_2 = np.array([[0,-1,-1],
                            [1,0,-1],
                            [1,1,0]])

kernel_emboss_3 = np.array([[-1,-1,0],
                            [-1,0,1],
                            [0,1,1]])

# Apply the embossing kernel to the image
embossed_img_1 = cv2.filter2D(img, -1, kernel_emboss_1)
embossed_img_2 = cv2.filter2D(img, -1, kernel_emboss_2)
embossed_img_3 = cv2.filter2D(img, -1, kernel_emboss_3)


plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(embossed_img_1, cv2.COLOR_BGR2RGB))
plt.title('Embossed img 1')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(embossed_img_2, cv2.COLOR_BGR2RGB))
plt.title('Embossed img 2')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(embossed_img_3, cv2.COLOR_BGR2RGB))
plt.title('Embossed img 3')
plt.axis('off')

plt.tight_layout()
plt.show()
