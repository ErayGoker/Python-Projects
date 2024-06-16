import cv2
import numpy as np

adileNasit=cv2.imread("images.jpeg")
#cv2.imshow("adile nasit",adileNasit)
#aynalananResim=cv2.copyMakeBorder(adileNasit,250,250,400,400,cv2.BORDER_REFLECT)
#cv2.imshow("adile nasit",aynalananResim)
#uzayanResim=cv2.copyMakeBorder(adileNasit,250,250,250,250,cv2.BORDER_REPLICATE)
#cv2.imshow("adile nasit",uzayanResim)
tekrarliResim=cv2.copyMakeBorder(adileNasit,190,190,190,190,cv2.BORDER_WRAP)
#kenarliResim=cv2.copyMakeBorder(adileNasit,35,35,35,35,cv2.BORDER_CONSTANT,value=(154,145,167))
dikdortgen=cv2.rectangle(tekrarliResim,(450,550),(650,230),(134,154,176),3)


cv2.imshow("adile nasit",tekrarliResim)



cv2.waitKey(0)
cv2.destroyAllWindows()