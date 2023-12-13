from djitellopy import tello
from cvzone.PoseModule import PoseDetector
import cv2


detector = PoseDetector()
cap = cv2.VideoCapture(0)
drone = tello.Tello()

drone.connect()
drone.takeoff()
drone.move_up(60)
drone.streamon()

for i in range(4):
    img = drone.get_frame_read().frame
    img = detector.findPose(img, draw=True)
    
    cv2.imshow("image", img)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
    drone.move_forward(30)
    drone.rotate_clockwise(45)
    

drone.land
