import cv2
import numpy as np

def add_gaussian_noise(image, mean=0, sigma=25):
    # Add Gaussian noise to the image
    row, col, ch = image.shape
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss
    return noisy.astype(np.uint8)

# Load the image
image = cv2.imread('./Data/test.jpg')

# Add Gaussian noise to the image
noisy_image = add_gaussian_noise(image)

# Save the noisy image
cv2.imwrite('./Data/noisy_image.jpg', noisy_image)

# Show the original image and the image with Gaussian noise
cv2.imshow('Original Image', image)
cv2.imshow('Noisy Image', noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()