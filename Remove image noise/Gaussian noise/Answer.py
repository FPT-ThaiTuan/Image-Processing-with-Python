import cv2
import numpy as np

# Read the image
image = cv2.imread('./Data/test.jpg')

# Apply median filter to remove noise
blurred_image = cv2.medianBlur(image, 5)

# Apply Gaussian filter to blur the image and remove noise
Gaussian_blurred_image = cv2.GaussianBlur(image, (5, 5), 1)

# Save result images
cv2.imwrite('./Data/blurred_image.jpg', blurred_image)
cv2.imwrite('./Data/Gaussian_blurred_image.jpg', Gaussian_blurred_image)

# Display the original image and processed images
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image (Median Filter)', blurred_image)
cv2.imshow('Gaussian Blurred Image', Gaussian_blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
