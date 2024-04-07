import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('./Data/test.jpg')

# Check if image is loaded properly
if img is None:
    print("Error: Image not found.")
    exit()

# Generate vignette mask using Gaussian kernels
rows, cols = img.shape[:2]
kernel_x = cv2.getGaussianKernel(cols, 200)
kernel_y = cv2.getGaussianKernel(rows, 200)
kernel = kernel_y * kernel_x.T
mask = 255 * kernel / np.linalg.norm(kernel)
output = np.copy(img)

# Applying the mask to each channel in the input image
for i in range(3):
    output[:, :, i] = output[:, :, i] * mask

# Convert BGR to RGB for displaying with Matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
output_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

# Display the images using Matplotlib
plt.figure(figsize=(10, 5))

# Original image
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title('Original')
plt.axis('off')

# Vignette image
plt.subplot(1, 2, 2)
plt.imshow(output_rgb)
plt.title('Vignette')
plt.axis('off')

plt.show()
