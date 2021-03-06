import cv2

model = cv2.face.LBPHFaceRecognizer_create()
model.read(
    '/home/pi/Documents/raspi-AIoT-test/model/aiot-faces.data'
    )
print('load training data done')

faceCascade = cv2.CascadeClassifier(
    '/home/pi/opencv/opencv-master/data/haarcascades/haarcascade_frontalface_alt2.xml'
    )

cap = cv2.VideoCapture(0)
cv2.namedWindow('video', cv2.WINDOW_AUTOSIZE)

names = ['Paul', 'Cloud']

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(gray, 1.1, 3)
    
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
        face_img = gray[y:y+h, x:x+w]
        face_img = cv2.resize(face_img, (400,400))
        
        val = model.predict(face_img)
                
        print('label:{}, confidence:{:.1f}'.format(val[0], val[1]))
        if val[1] < 50:
            cv2.putText(frame, names[val[0]], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                    
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == 27:
        cap.release()
        cv2.destroyAllWindows()
        break