import cv2 as cv

haar_kaskada = cv.CascadeClassifier("cat_face_detector.xml")
cap = cv.VideoCapture(0) #jedina promena u odnosu na prethodnu realizaciju je sto se video ne ucitava iz fajl sistema, nego preko web kamere
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cat_faces = haar_kaskada.detectMultiScale(gray, 1.05,20)
    for(x, y, w, h) in cat_faces:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
    cv.imshow('Video snimak', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

cv.waitKey(0)