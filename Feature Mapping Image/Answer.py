import cv2

# Read the image
image = cv2.imread('./Data/test.jpg')

# Initialize the SIFT and ORB feature extractors
sift = cv2.SIFT_create()
orb = cv2.ORB_create()

# Find keypoints and descriptors for SIFT
keypoints_sift, descriptors_sift = sift.detectAndCompute(image, None)
# Find keypoints and descriptors for ORB
keypoints_orb, descriptors_orb = orb.detectAndCompute(image, None)

# Draw keypoints on the image for SIFT and ORB
image_with_keypoints_sift = cv2.drawKeypoints(image, keypoints_sift, None)
image_with_keypoints_orb = cv2.drawKeypoints(image, keypoints_orb, None)

# Display the original image and images with keypoints using OpenCV
cv2.imshow('Original Image', image)
cv2.imshow('SIFT Keypoints', image_with_keypoints_sift)
cv2.imshow('ORB Keypoints', image_with_keypoints_orb)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
