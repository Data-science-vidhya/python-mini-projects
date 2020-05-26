import cv2
# read image
image = cv2.imread("image 2.jpg")

# convert image in to gray scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray cat", gray_image)
# save image file 
cv2.imwrite("Gray cat.jpg", gray_image)

# print image
cv2.imshow("image 2.jpg", image)
# delay
cv2.waitKey(0)
cv2.destroyAllWindows()