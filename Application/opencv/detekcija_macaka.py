import cv2 as cv

#ucitavanje zeljene slike
img = cv.imread('photos/macke.jpg')

#konvertovanje slike u grayscale rezim
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Siva macka', gray)

haar_kaskada = cv.CascadeClassifier("cat_face_detector.xml")

#promena parametara funkcije detectMultiScale ima veliki uticaj na detektovane objekte
macka_pravougaonik = haar_kaskada.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
print(f'Broj nadjenih macaka je= {len(macka_pravougaonik)}')
for (i,(x, y,w, h)) in enumerate(macka_pravougaonik):
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0) , thickness=3)
    cv.putText(img, "Macka #{}".format(i + 1), (x, y - 10),
		cv.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)
cv.imshow('Prepoznate macke', img)
cv.waitKey(0)