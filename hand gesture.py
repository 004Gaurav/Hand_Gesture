import cv2                #(pip install opencv-python) An open-source framework for building pipelines to perform computer vision inference over arbitrary sensory data such as video or audio #
import mediapipe as mp    # (pip install mediapipe)     Loads an image from the specified file #
import time               # (pip install time-python)   The code above imports the time module, measures the time taken to execute the code between "Start" and "End" using time.time(), and then calculates the elapsed time #

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c= img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                if id == 0:
                    cv2.circle(img, (cx,cy), 25, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(10,78), cv2.FONT_HERSHEY_PLAIN,3,
                (255,0,255), 3)


    cv2.imshow("Image", img)
    cv2.waitKey(1)



