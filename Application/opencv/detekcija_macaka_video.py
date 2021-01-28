import cv2 as cv

haar_kaskada = cv.CascadeClassifier("cat_face_detector.xml")
#reskaliranje frejma je vrseno zbog boljih rezultata detekcije
def rescaleFrame(frame, scale =0.40):
    width = int(frame.shape[1]*scale)
    height= int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)
cap = cv.VideoCapture('videos/macka1.mp4')
while(cap.isOpened()):
    ret, frame = cap.read()
    frame_resized = rescaleFrame(frame)
    gray = cv.cvtColor(frame_resized, cv.COLOR_BGR2GRAY)
    cat_faces = haar_kaskada.detectMultiScale(gray, 1.1,2)
    for(x, y, w, h) in cat_faces:
        cv.rectangle(frame_resized, (x,y), (x+w, y+h), (0, 255, 0), 2)
    cv.imshow('Video snimak', frame_resized)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

cv.waitKey(0)