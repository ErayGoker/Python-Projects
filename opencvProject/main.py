import cv2
import numpy as np

#resim=cv2.imread("2020-Yamaha-MT250-EU-Ice_Fluo-Static-003-03.jpg")
#resim2=cv2.imread("417VqJLN-7L._AC_UF1000,1000_QL80_.jpg")

#cv2.imshow("mt25 resmi",resim)
#cv2.imwrite("griMT25.png",resim)
#print(resim[(5,8)])
#print("size : ", resim.size)
#print(resim.dtype)
#print(resim.shape)

#resim2[50,5]=[25,25,25]
#for x in range(200):
#    resim2[150,x]=[0,0,0]
#cv2.imshow("beyazKagit",resim2)

#cv2.waitKey(0)
#cv2.destroyAllWindows()



eray=cv2.imread("WhatsApp Image 2024-02-22 at 12.23.07.jpeg")
eray[80:120,105:215,]=[23,43,23]
cv2.imshow("erayCV",eray)


cv2.waitKey(0)
cv2.destroyAllWindows()