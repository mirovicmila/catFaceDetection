import cv2 as cv
import numpy as np
# ako zelimo da radimo sa praznom slikom tj da je sami kreiramo
blank = np.zeros((500, 500, 3), dtype='uint8')
# 500, 500, 3 znaci sirina, visina i broj kanala za boje
#cv.imshow('Prazno', blank)
# ako zelimo da radimo sa slikom koja vec postoji
img = cv.imread('../photos/liza.jpg')
#cv.imshow('Macka', img)
# bojimo sliku nekom bojom
# blank[:]= 0,255,0 #pristupamo svim pikselima slike i postavljamo njihovu vrednost na zelenu
blank[200:300, 300:400] = 0, 0, 255
# mozemo da crtamo pravougaonik
cv.rectangle(img, (0, 0),
             (img.shape[1]//2,img.shape[0]//2), (0, 255, 0), thickness=cv.FILLED)

#cv.imshow('Zeleno', blank)
#moze da se crta i krug
cv.circle(img, (250,250), 40, (0,0,255), thickness=-1) #ako se thickness stavi na -1 to znaci da se vrsi ispuna
#ovde su parametri centar kruga, poluprecnik, boja i debljina linije kojom je iscrtan
#vodi racuna da je BGR konvencija, a ne RGB
#cv.imshow('Krug',blank)
#crtanje li
cv.line(img, (0,0) ,(250,250), (255,0,0), thickness=3)
#cv.imshow('Linija',blank)
#pisanje teksta po slici
cv.putText(img, 'Macka', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
cv.imshow('Prikaz crtanja po slici', img)
cv.waitKey(0)
