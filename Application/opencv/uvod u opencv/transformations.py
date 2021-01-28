import cv2 as cv
import numpy as np
img = cv.imread('../photos/liza.jpg')

#cv.imshow('Macka', img)
#translacija- levo,dole,gore,desno
def translate(img, x, y): 
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions= (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
# -x --> znaci da radimo translate levo
# -y --> znaci da radimo translate gore
# x  --> znaci da radimo translate desno
# y  --> znaci da radimo translate dole
translated = translate(img, 100, 100) #ovo ce da translira sliku za 100p desno po x-osi i 100p dole po y-osi
#cv.imshow('Translirana',translated)
#Rotacija slike za neki ugao
def rotate(img, angle, rotPoint= None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint= (width//2, height//2) #ako ne specificiramo ugao rotacije, onda stavljamo da to bude centar
    rotMat= cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions= (width, height)
    return cv.warpAffine(img, rotMat, dimensions)
rotated = rotate(img, 45) #ovo ce sliku da rotira za 45 stepeni u odnosu na centar
#rotacija ide u suprotnom smeru od kazaljke na satu, ako zelimo u smeru kazaljke na satu, onda je ugao negativan
#cv.imshow('Rotirana macka', rotated)
#ako zelimo da uradimo rotaciju rotirane slike, moze da dodje do problema
druga_rotirana = rotate(rotated, 45);
#cv.imshow('Rotacija rotacije', druga_rotirana)
#do problema dolazi jer ce se vrsiti i rotacija crnih trouglova na slici, odnosno to su delovi slike koji ne postoje
#ali su vidljivi pri rotaciji
#zato je bitno prilikom rotacije odmah staviti finalni ugao rotacije, a ne menjati taj ugao kroz vise poziva rotate funkcije
#Resize slike
resized = cv.resize(img, (300,300), interpolation= cv.INTER_CUBIC)
#cv.imshow('Resized',resized)
#Flipping slike
flip=cv.flip(img, -1)
# 0 znaci flip preko x-ose 
# 1 znaci flip preko y-ose
# -1 znaci i horizontalno i vertikalno
cv.imshow('Flip macke', flip)
#Cropp slike
cropped = img[200:400, 300:400]
#cv.imshow('Cropped', cropped)

cv.waitKey(0)