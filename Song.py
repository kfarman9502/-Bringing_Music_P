import time
import cv2
import webbrowser
from cvzone.HandTrackingModule import HandDetector
import pyautogui

model = HandDetector()

cap = cv2.VideoCapture(0)

while True:
    status, photo = cap.read()
    cv2.imshow("doll", photo)
    if cv2.waitKey(50) == 13:
        break
    hand = model.findHands(photo, draw = False)  
    if hand:
        handphoto = hand[0]
        fingersup = model.fingersUp(handphoto)
        if fingersup == [0, 0, 0, 0, 0]:            #to play/pause
            pyautogui.moveTo(554, 390, duration=0.0)
            pyautogui.click()
            time.sleep(1)
        elif fingersup == [0, 1, 0, 0, 0]:
            webbrowser.open("https://music.youtube.com/watch?v=UNOtbkQxECI")
            time.sleep(1)
            print("Playing....Mood")
        elif fingersup == [0, 1, 1, 0, 0]:
            webbrowser.open("https://music.youtube.com/watch?v=VKC_hzJ3jzg&list=RDAMVMMMfpp0-lnw4")
            time.sleep(1)
            print("Playing....Señorita")
        elif fingersup == [0, 1, 1, 1, 0]:
            webbrowser.open("https://music.youtube.com/watch?v=ORrFJ63nlcA&list=RDAMVMORrFJ63nlcA")
            time.sleep(1)
            print("Playing....Perfect")
        elif fingersup == [0, 1, 1, 1, 1]:
            webbrowser.open("https://music.youtube.com/watch?v=XfEMj-z3TtA&list=RDAMVMXfEMj-z3")
            time.sleep(1)
            print("Playing....STAY")
        elif fingersup == [1, 1, 1, 1, 1]:
            webbrowser.open("https://music.youtube.com/watch?v=Hx4nWW9z0ig&list=RDAMVMXfEMj-z3TtA")
            time.sleep(1)
            print("Playing....Dance Monkey")
        else:
            print("sorry")
            
   # else:
      #  time.sleep(10)
       # break
cv2.destroyAllWindows()
cap.release()
