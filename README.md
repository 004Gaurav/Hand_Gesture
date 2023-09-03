# Hand_Gesture
This Python script uses OpenCV and Mediapipe to perform hand tracking on a webcam feed. Here's a summary of what the code does:

1. **Import Libraries**: The code begins by importing the necessary libraries:
   - `cv2`: OpenCV for computer vision tasks.
   - `mediapipe as mp`: Mediapipe library for hand tracking.
   - `time`: Python's time library for measuring elapsed time.

2. **Initialize VideoCapture**: It initializes a `VideoCapture` object to access the default camera (usually the webcam).

3. **Load Hand Tracking Module**: The Mediapipe hand tracking module is loaded and an instance of the `Hands` class is created for hand tracking.

4. **Initialize Variables**: `pTime` and `cTime` are initialized to store previous and current times for calculating the frames per second (FPS).

5. **Main Loop**:
   - The main loop runs indefinitely.
   - Inside the loop, it reads a frame from the webcam using `cap.read()`.
   - Converts the BGR image to RGB, which is required by Mediapipe.
   - Processes the RGB image to detect hands and stores the results in the `results` variable.

6. **Hand Landmark Detection**:
   - If one or more hands are detected (`results.multi_hand_landmarks` is not empty), it iterates through each detected hand.
   - For each hand, it loops through each landmark and retrieves its pixel coordinates (`cx` and `cy`) based on normalized positions.
   - It prints the landmark ID and pixel coordinates, and if the ID is 0 (center of the palm), it draws a filled purple circle around it.
   - It also draws the hand landmarks and connections on the image using `mpDraw.draw_landmarks`.

7. **Calculate FPS**:
   - The script calculates the frames per second (FPS) by measuring the time taken for each frame to process.

8. **Display FPS on Image**:
   - It displays the FPS value as text on the image using `cv2.putText`.

9. **Display Image**:
   - The processed image with landmarks and FPS information is displayed in a window using `cv2.imshow`.

10. **Wait for Key Press**:
    - It waits for 1 millisecond for a key press to allow the image window to refresh in the loop.

Overall, this script continuously captures webcam frames, detects and tracks hand landmarks, and displays the frames with landmarks and FPS information in real-time. It's a simple example of using computer vision and hand tracking for real-time applications, such as gesture recognition or interactive applications.
