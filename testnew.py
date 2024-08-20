#Virtual Mouse, Open CV project by Ganga
import cv2
import numpy as np
import TrackingModule as htm
import time
import pyautogui

# Camera and variables setup
#wCam, hCam: Dimensions of the camera feed.
wCam, hCam = 1380, 820
frameR = 100  # Frame Reduction
smoothening = 7 #smoothening: Smoothing factor for cursor movement.
pTime = 0 #pTime: Previous time for FPS calculation.
plocX, plocY = 0, 0 #plocX, plocY: Previous cursor location.
clocX, clocY = 0, 0 #clocX, clocY: Current cursor location.
screenshot_count= 0
#Initialize Camera 

# cap: Captures video from the camera.
# cap.isOpened(): Checks if the camera is accessible.

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Camera not found or not accessible.")
    exit()

cap.set(3, wCam)
cap.set(4, hCam)

# cap.set(3, wCam): Sets the width of the video.
# cap.set(4, hCam): Sets the height of the video.

#Initialize hand detector

#detector: Initializes the hand detector with a maximum of one hand.
detector = htm.handDetector(maxHands=1)
wScr, hScr = pyautogui.size()  # Get screen width and height

while True:
    success, img = cap.read()
    if not success:
        print("Error: Failed to capture image.")
        break
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]  # Index finger tip
        x2, y2 = lmList[12][1:]  # Middle finger tip

        fingers = detector.fingersUp()
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

        # Moving cursor
        if fingers[1] == 1 and fingers[2] == 0:
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening
            pyautogui.moveTo(clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

        # Clicking
        if fingers[1] == 1 and fingers[2] == 1:
            length, img, lineInfo = detector.findDistance(8, 12, img)
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                pyautogui.click()

        # Right Click (thumb and index finger up)
        if fingers[0] == 1 and fingers[1] == 1 and all(finger == 0 for finger in fingers[2:]):
            length, img, lineInfo = detector.findDistance(4, 6, img)
            if length < 30:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 255), cv2.FILLED)
                pyautogui.rightClick()  # Perform a righft-click

        # Scrolling (thumb up gesture and pinky)
        if fingers[0] == 1 and all(finger == 0 for finger in fingers[1:]):
            pyautogui.scroll(100)  # Scroll up
        if fingers[0] == 0 and fingers[4] == 1 and all(finger == 0 for finger in fingers[1:4]):
            pyautogui.scroll(-100)  # Scroll down

        # Screenshot (all fingers up gesture)
        if all(finger == 1 for finger in fingers):
            screenshot_filename = f'screenshot_1{screenshot_count}.png'
            pyautogui.screenshot(screenshot_filename)
            screenshot_count+= 1
            time.sleep(1)  # Wait to avoid multiple screenshots

    # FPS Calculation
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    # Display and exit
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
#add drag to and other functions as required.
#Ganga 
