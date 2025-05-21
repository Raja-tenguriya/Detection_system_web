import cv2
cap = cv2.VideoCapture(0)
mode = 'normal'

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if mode == 'gray':
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif mode == 'blur':
        frame = cv2.GaussianBlur(frame, (15, 15), 0)
    elif mode == 'edge':
        frame = cv2.Canny(frame, 100, 200)

    cv2.imshow("Live Filter App", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('g'):
        mode = 'gray'
    elif key == ord('b'):
        mode = 'blur'
    elif key == ord('e'):
        mode = 'edge'
    elif key == ord('n'):
        mode = 'normal'

cap.release()
cv2.destroyAllWindows()
