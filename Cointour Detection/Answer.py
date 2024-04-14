import cv2
import numpy as np

# Read the image
coins = cv2.imread('./Data/test.png')

# Convert the image to grayscale
gray = cv2.cvtColor(coins, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary image
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Find contours in the binary image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter out contours larger than a specific threshold
large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 1000]

# Get the number of large contours found
num_large_contours = len(large_contours)

# Create a copy of the original image to draw bounding boxes
bounding_img = np.copy(coins)

# Iterate over each large contour and draw bounding rectangle
for contour in large_contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(bounding_img, (x, y), (x + w, y + h), (0, 255, 0), 3)

# Display the image with bounding boxes
cv2.putText(bounding_img, f'Number of large contours: {num_large_contours}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
cv2.imshow('Bounding Boxes', bounding_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
