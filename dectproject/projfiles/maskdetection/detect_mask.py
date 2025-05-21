import cv2
import numpy as np
import tensorflow as tf

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

model = tf.keras.models.load_model("mask_detector_model.h5")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w] 
        face = cv2.resize(face, (64, 64))  
        face = np.array(face) / 255.0  
        face = np.expand_dims(face, axis=0)  

        result = model.predict(face)[0]  # Predict
        label = "Mask" if np.argmax(result) == 1 else "No Mask"

        color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("Mask Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()



