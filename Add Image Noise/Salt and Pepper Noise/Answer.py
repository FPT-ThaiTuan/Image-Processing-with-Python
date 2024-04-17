import random 
import cv2 

def add_salt_and_pepper_noise(img): 
    # Getting the dimensions of the image 
    rows, cols = img.shape 
      
    # Add salt noise
    salt_pixels = random.randint(300, 10000) 
    for _ in range(salt_pixels):
        y_coord = random.randint(0, rows - 1)
        x_coord = random.randint(0, cols - 1)
        img[y_coord][x_coord] = 255
        
    # Add pepper noise
    pepper_pixels = random.randint(300, 10000) 
    for _ in range(pepper_pixels):
        y_coord = random.randint(0, rows - 1)
        x_coord = random.randint(0, cols - 1)
        img[y_coord][x_coord] = 0
        
    return img 

# Read the color image in grayscale
img = cv2.imread('./Data/test.jpg', cv2.IMREAD_GRAYSCALE) 
  
# Add salt-and-pepper noise
noisy_img = add_salt_and_pepper_noise(img)

# Store the noisy image
cv2.imwrite('./Data/salt_and_pepper_lena.jpg', noisy_img)
