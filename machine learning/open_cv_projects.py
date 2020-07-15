import cv2

img1=cv2.imread("Resources/Deepika-Padukone-950x1689.jpg")
# print(img1.shape)
img2 = cv2.resize(img1,(int(950/2),(int(1689/2))))
img3 = img2[0:644, :]

print(img2.shape)
cv2.imshow("output", img3)
cv2.waitKey(0)

cv2.destroyAllWindows()
