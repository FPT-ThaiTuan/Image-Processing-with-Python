import cv2

# Open a video capture object
# Change the link so the video can be read
cap = cv2.VideoCapture(0)

# To check if the video has opened successfully of not
if not cap.isOpened():
    print("Error: Couldnot open the video.")
    exit()

# Loop through the video frames
while True:
    # Reading a frame from the video
    ret, frame = cap.read()

    # Break the loop if the video has ended
    if not ret:
        break

    # Display the original frame
    cv2.imshow('Original Video', frame)

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Black and White Video', gray_frame)

    # Perform edge detection on the video
    edges_frame = cv2.Canny(gray_frame, 50, 150)
    cv2.imshow('Edges Video', edges_frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()