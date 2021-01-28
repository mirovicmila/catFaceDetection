import cv2 as cv
img = cv.imread('../photos/liza.jpg')
#cv.imshow('Macka', img)
#prebacivanje slike u grayscale
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Grayscale macka', gray)
#blur slike
blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
#voditi racuna o srednjem parametru, on nam kaze koliki blur primenjujemo
#ako stavimo (3,3) blur ce da bude manji, a ako stavimo (7,7) bice vise zamuceno
#cv.imshow('Mutna macka', blur)
#trazenje ivica (edge cascade)
canny = cv.Canny(blur, 125, 175)
#ako Canny funkciji kao parametar prosledimo blur umesto img onda cemo imati manje ivica
#ukoliko zelimo vise ivica tj detaljniji prikaz, onda prosledimo img kao parametar                                                                                                                                                   metar
#cv.imshow('Canny macka', canny)
#Dilating slike
dilated = cv.dilate(img, (9,9), iterations=3)
#ovde se desava da ivica postaju bolje vidljive, sto je veci srednji parametar to je debljina ivica veca
#osim toga, da bi promene bile jos uocljivije, potrebno je povecati broj iteracija
cv.imshow('Dilated',dilated)
#Eroding slike
eroded = cv.erode(dilated, (3,3) , iterations=3)
#cv.imshow('Eroded', eroded)
#ovo bi nam sluzilo ako zelimo da na osnovu dilated slike rekonstruisemo pocetne ivice tj canny sliku
#dobije se skoro isti edge cascade
#Resize slike
resized = cv.resize(img, (500,500))
#cv.imshow('Resized', resized)
#Crop slike
cropped = img[50:200, 200:400] #ovo mozemo da radimo jer su slike zapravo nizovi 
#cv.imshow('Cropped', cropped)

cv.waitKey(0)