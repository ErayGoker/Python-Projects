import cv2
import numpy as np

onder=cv2.imread("Onder.jpeg")
arda=cv2.imread("WhatsApp Image 2024-05-12 at 14.44.35.jpeg")

#cv2.imshow("onder",onder)
#kesitOnder=onder[500:700,350:850]
#cv2.imshow("kestiOnder",kesitOnder)
kesit2=arda[600:800,400:900]
kesit2[:,:,0]=55
kesit2[:,:,1]=35


onder[550:750,350:850]=kesit2


cv2.imshow("ardaKesit",onder)



cv2.waitKey(0)
cv2.destroyAllWindows()