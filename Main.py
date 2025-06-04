import cv2

img = cv2.imread("bag.png",0)
img1 = cv2.resize(img,(0,0),fx=7,fy=7)
cv2.imwrite("plastic_bag.png",img1)
cv2.imshow("bag image", img)
cv2.imshow("big bag theory", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#colour => (1)
#grayscale => (0)
#unchanged => (-1)

# image = cv2.imread("bird.png", 1)
# B, G, R = cv2.split(image)

# cv2.imshow("original", image)
# cv2.waitKey(0)

# cv2.imshow("Blue Saturation Image", B)
# cv2.waitKey(0)

# cv2.imshow("Green Saturation Image", G)
# cv2.waitKey(0)

# cv2.imshow("Red Saturation Image", R)
# cv2.waitKey(0)

# cv2.destroyAllWindows()
