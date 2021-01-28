import cv2 as cv
import numpy as np
img = cv.imread('../photos/liza.jpg')
#cv.imshow('Macke', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Crno bela macka', gray)
blank= np.zeros(img.shape, dtype='uint8')
#cv.imshow('Blank', blank) #ovo nam je prazna slika 
canny = cv.Canny(img, 125, 175)
#cv.imshow('Canny ivice', canny)
ret, thresh = cv.threshold(gray,125,255, cv.THRESH_BINARY) #125 je threshold vrednost, a 255 je maksimalna vrednost
#threshold radi binarizaciju slike tj pretvara je u binarnu formu
#ako je piksel ispod 125 on postaje crn
#ako je piksel iznad 125 on postaje beo
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#RETR_LIST znaci da zelimo sve konture slike, a ne samo eksterne, RETL_EXTERNAL bi vratilo samo eksterne konture
#CHAIN_APPROX_NONE vs CHAIN_APPROX_SIMPLE --> ako imamo recimo liniju, prva ce da vrati koordinate svih tacaka, a druga koordinate pocetka i kraja
#nacin na koji radi funckija findContours je da ce da vrati konture i hijerarhije
#konture su python lista koordinata koje su nadjene na slici
#hijerarhije su nacin reprezentacije kontura kad imamo vise ugnjezdenih objekata
#ako bismo uradili blur slike imali bismo manje kontura, razlika je znacajna
print(f'{len(contours)} kontura nadjeno!')
cv.imshow('Nakon binarizacije', canny)
#cv.drawContours(blank, contours, -1, (0,0,255), 1) #crta konture po praznoj slici
#-1 nam je index konture tj koliko kontura zelimo, -1 znaci da zelimo sve
#cv.imshow('Nacrtane konture', blank)
cv.waitKey(0)