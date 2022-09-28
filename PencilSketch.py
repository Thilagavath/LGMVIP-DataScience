import cv2
image = cv2.imread("me.jpeg")#imread-string representing the path of the image to be read.
cv2.imshow("Me", image)#imshow-string representing the name of the window in which image to be displayed. 
cv2.waitKey(0)#waitkey-Waits untill any key is pressed
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Me", gray_image)
cv2.waitKey(0)
inverted_image = 255 - gray_image
cv2.imshow("Inverted", inverted_image)
cv2.waitKey()
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)
cv2.imshow("original image", image)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)
