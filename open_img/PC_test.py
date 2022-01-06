import cv2 as cv

print('Hello World')

img_rgb = cv.imread('Lenna.jpg') 

cv.imshow('test',img_rgb)
cv.waitKey(5000)
