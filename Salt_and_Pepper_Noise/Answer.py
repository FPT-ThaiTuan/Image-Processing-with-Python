
import numpy as np
import cv2
import scipy.signal

def meanFilter(image, string):
  kernel_size = 3 
  kernel = np.ones((kernel_size, kernel_size), dtype="float") * (0.5 / (kernel_size * kernel_size))
  kernel = np.flipud(np.fliplr(kernel))     
  padImage=np.pad(image,((1, 1), (1, 1)), string)
  filter = scipy.signal.convolve2d(padImage, kernel, mode='same', boundary='fill', fillvalue=0) 
  return filter


path = "./Image/XrayCircuitBoardWithSaltnPepperNoise.png"
image = cv2.imread(path, 0)

result = meanFilter(image, 'edge')

cv2.imshow('Origin Image',image)
cv2.imshow('Result Image',result.astype(np.uint8))

# Lưu ảnh kết quả
cv2.imwrite("./Data/Filtered_Image.png", result.astype(np.uint8))

cv2.waitKey(0)
cv2.destroyAllWindows()