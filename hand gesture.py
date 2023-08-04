import cv2                # Import OpenCV library - Used for computer vision tasks
import mediapipe as mp    # Import Mediapipe library - Used for hand tracking
import time               # Import time library - Used for measuring elapsed time

cap = cv2.VideoCapture(0)  # Initialize VideoCapture object to access the default camera (usually the webcam)

mpHands = mp.solutions.hands  # Load the Mediapipe hand tracking module
hands = mpHands.Hands()      # Create an instance of the Hands class for hand tracking
mpDraw = mp.solutions.drawing_utils  # Utility class for drawing hand landmarks on images

pTime = 0  # Initialize variable to store previous time (for calculating FPS)
cTime = 0  # Initialize variable to store current time (for calculating FPS)

while True:
    success, img = cap.read()  # Read a frame from the webcam
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert the BGR image to RGB (required by Mediapipe)
    results = hands.process(imgRGB)  # Process the RGB image to detect hands
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:  # Check if any hands are detected in the frame
        for handLms in results.multi_hand_landmarks:  # Loop through each detected hand
            for id, lm in enumerate(handLms.landmark):  # Loop through each landmark of the hand
                # Get the pixel coordinates (cx, cy) of the landmark based on its normalized position (lm.x, lm.y)
                h, w, c = img.shape  # Get the height, width, and number of channels of the image
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)  # Print the ID of the landmark and its pixel coordinates on the console
                if id == 0:  # If the landmark ID is 0 (the center of the palm), draw a filled purple circle around it
                    cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)  # Draw the hand landmarks and connections on the image

    cTime = time.time()  # Record the current time in seconds
    fps = 1 / (cTime - pTime)  # Calculate the frames per second (FPS) by taking the reciprocal of the time difference
    pTime = cTime  # Update pTime to be the same as cTime for the next iteration

    # Display the FPS value as text on the image
    cv2.putText(img, str(int(fps)), (10, 78), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)  # Display the processed image with landmarks and FPS information
    cv2.waitKey(1)  # Wait for 1 millisecond for a key press to allow the image window to refresh in the loop
