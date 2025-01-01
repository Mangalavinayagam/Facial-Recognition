import threading

import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

face_match1 = False
face_match2 = False
face_match3 = False

reference_img = cv2.imread("Photo1.jpg")
reference_img2 = cv2.imread("Photo2.jpeg")
reference_img3 = cv2.imread("Photo3.jpeg")

def check_face(frame):
    global face_match1, face_match2, face_match3
    try:
        if DeepFace.verify(frame, reference_img.copy())['verified']:
            face_match1 = True
        elif DeepFace.verify(frame, reference_img2.copy())['verified']:
            face_match2 = True
        elif DeepFace.verify(frame, reference_img3.copy())['verified']:
            face_match3 = True
        else:
            face_match1,face_match2,face_match3 = False,False,False
    except ValueError:
        face_match1 = False
        face_match2 = False
        face_match3 = False

while True:
    ret,frame=cap.read()
    
    if ret:
        if counter % 30==0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter+=1
        
        if face_match1:
            cv2.putText(frame, "Person1", (20,450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0),3)
        elif face_match2:
            cv2.putText(frame, "Person2", (20,450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0),3)
        elif face_match3:
            cv2.putText(frame, "Person3", (20,450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0),3)
        else:
            cv2.putText(frame, "NO MATCH", (20,450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255),3)
        cv2.imshow("Video",frame)        
    key=cv2.waitKey(1)
    if key==ord("q"):
        break

    
cv2.destroyAllWindows()
