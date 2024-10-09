import cv2
import numpy as np

# Function to handle trackbar position and apply color changes dynamically
def empty(a):
    pass

# Create a window for the result
cv2.namedWindow("Result")

# Create trackbars for changing colors for green and brown regions
cv2.createTrackbar("Brown - B", "Result", 65, 255, empty)
cv2.createTrackbar("Brown - G", "Result", 150, 255, empty)
cv2.createTrackbar("Brown - R", "Result", 240, 255, empty)

cv2.createTrackbar("Green - B", "Result", 179, 255, empty)
cv2.createTrackbar("Green - G", "Result", 250, 255, empty)
cv2.createTrackbar("Green - R", "Result", 25, 255, empty)

# Loop through 10 images
for i in range(1, 11):
    # Image path in the uassampleimage folder
    img_path = f'C:/Users/Md Asif/Desktop/uassampleimage/{i}.png'
    img = cv2.imread(img_path)

    # Check if the image was successfully loaded
    if img is None:
        print(f"Image {i}.png not found or can't be opened at {img_path}")
        continue

    while True:
        # Convert the image from BGR to HSV color space
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Define the lower and upper range for green in HSV
        lower_green = np.array([37, 0, 0])
        upper_green = np.array([55, 255, 255])
        mask_green = cv2.inRange(hsv, lower_green, upper_green)

        # Define the lower and upper range for brown in HSV
        lower_brown = np.array([5, 50, 0])
        upper_brown = np.array([25, 255, 255])
        mask_brown = cv2.inRange(hsv, lower_brown, upper_brown)

        # Get color values from the trackbars
        brown_b = cv2.getTrackbarPos("Brown - B", "Result")
        brown_g = cv2.getTrackbarPos("Brown - G", "Result")
        brown_r = cv2.getTrackbarPos("Brown - R", "Result")

        green_b = cv2.getTrackbarPos("Green - B", "Result")
        green_g = cv2.getTrackbarPos("Green - G", "Result")
        green_r = cv2.getTrackbarPos("Green - R", "Result")

        # Change brown regions to the color selected by trackbars
        img[mask_brown > 0] = (brown_b, brown_g, brown_r)

        # Change green regions to the color selected by trackbars
        img[mask_green > 0] = (green_b, green_g, green_r)

        # Display the modified image
        cv2.imshow("Result", img)

        # Break the loop on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Close all OpenCV windows after the loop
cv2.destroyAllWindows()