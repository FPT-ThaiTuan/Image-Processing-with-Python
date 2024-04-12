import cv2

# open an image using opencv
imgOriginal = cv2.imread('./Data/test.jpg')
img = cv2.resize(imgOriginal, (640, 304))

cv2.imshow('Origin Image', img)

# get image height and width
height, width, channels = img.shape

# add watermark
white = (255, 255, 255)
position = (width - 125, height - 15)
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img, "TuanDDT", 
    position, font, 0.7, white, 1)

cv2.imshow('TuanDDT - Watermark', img)

# save image using opencv
cv2.imwrite('./Image/OfficeWatermark.jpg', img)

# key controller
cv2.waitKey(0)
cv2.destroyAllWindows()