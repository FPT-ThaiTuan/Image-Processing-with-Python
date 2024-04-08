import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
img = cv2.imread('./Data/test.png')

# Create filter matrices
kernel_1 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
kernel_2 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

# Apply the filter matrices to the image
sharpened_1 = cv2.filter2D(img, -1, kernel_1)
sharpened_2 = cv2.filter2D(img, -1, kernel_2)

# Display the images using Matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(sharpened_1, cv2.COLOR_BGR2RGB))
plt.title('Sharpened Image 1')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(sharpened_2, cv2.COLOR_BGR2RGB))
plt.title('Sharpened Image 2')
plt.axis('off')

plt.tight_layout()
plt.show()

# Save the sharpened images
cv2.imwrite('./Data/sharpened_image_1.png', sharpened_1)
cv2.imwrite('./Data/sharpened_image_2.png', sharpened_2)
