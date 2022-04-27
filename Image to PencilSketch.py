import cv2
#readtheimage
image = cv2.imread("image.jpg")
cv2.imshow("Actor", image)
cv2.waitKey(0)
#after reading the image, we will create a new image by converting the original image to greyscale:
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("New Actor", gray_image)
cv2.waitKey(0)
#the next step is to invert the new grayscale image:
inverted_image = 255 - gray_image
cv2.imshow("Inverted", inverted_image)
cv2.waitKey(0)
#the next step in the process is to blur the image by using the Gaussian Function in OpenCV
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
#image to pencil sketch
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)