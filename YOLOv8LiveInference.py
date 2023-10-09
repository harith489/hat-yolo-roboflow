from ultralytics import YOLO

import cv2

model = YOLO('yolov8m.pt')
model = YOLO("C:\\Users\\User\\Documents\\Project\\yolo\\best.pt")


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    results = model.predict(frame, show=True, conf=0.5)
   

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()