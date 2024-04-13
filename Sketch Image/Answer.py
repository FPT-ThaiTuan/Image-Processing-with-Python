import cv2
import matplotlib.pyplot as plt

# Read the image from file
img = cv2.imread('./Data/test.jpg', 0)

# Read the image in BGR format
# Convert BGR to RGB
imgRGB = cv2.cvtColor(cv2.imread('./Data/test.jpg', 1), cv2.COLOR_BGR2RGB)

# Invert the image
inverted = 255 - img

# Blur the inverted image
blurred = cv2.GaussianBlur(inverted, (21, 21), 0)

# Invert the blurred image
inverted_blurred = 255 - blurred

# Create a pencil sketch by dividing the original image by the inverted blurred image
sketch = img / inverted_blurred
sketch = sketch * 255

# Save the sketch to a file
cv2.imwrite('./Data/result.jpg', sketch)

# Display the original and edited images using matplotlib
plt.figure(figsize=(10,5))

# Display the original image
plt.subplot(1, 2, 1)
plt.imshow(imgRGB)
plt.title('Original Image')
plt.axis('off')

# Display the edited image
plt.subplot(1, 2, 2)
plt.imshow(sketch, cmap='gray')
plt.title('Sketch Image')
plt.axis('off')

# Show both images simultaneously
plt.show()
