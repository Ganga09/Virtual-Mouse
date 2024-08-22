Virtual Mouse

This project involves the development of a virtual mouse that is controlled entirely by hand gestures. 
The MediaPipe's Hand Landmarks module accurately tracks and detects hand movements in real time.
Various hand gestures are mapped to corresponding mouse functions, such as;
1) index finger up to move the cursor
2) index and middle fingers up for left-click
3) index finger and thumb up for right-click
4) thumb for scrolling up and pinky finger for scrolling down.
5) all fingers out for screenshot

PyAutoGUI is employed to simulate these mouse actions. 
Mediapipe:
* The MediaPipe Hand Landmarker detect the landmarks of the hands in an image. 
* It can be used to locate key points of hands and render visual effects on them.
* The Hand Landmarker model bundle contains a palm detection model and a hand landmarks detection model
* Hand Landmarker uses the bounding box defined by the hand landmarks model in one frame to localize the region of hands for subsequent frames.

![image](https://github.com/user-attachments/assets/a68089b9-9958-49cf-9e58-74a3d7738478)

  

PyAutoGUI lets your Python scripts control the mouse and keyboard to automate interactions with other applications. 
PyAutoGUI has several features:

* Moving the mouse and clicking in the windows of other applications.
* Sending keystrokes to applications (for example, to fill out forms).
* Take screenshots, and given an image (for example, of a button or checkbox), and find it on the screen.
* Locate an application’s window, and move, resize, maximize, minimize, or close it (Windows-only, currently).
* Display alert and message boxes.

The virtual mouse provides a user-friendly touch-free interface and a solution for gesture-based control in everyday computing tasks.

![screenshot_17](https://github.com/user-attachments/assets/f1c0ec1c-0867-4b07-8309-9250f0acfe39)
