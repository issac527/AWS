# 원래 1일듯. OpenCV - gray scale 및 labeling과정
import cv2

image = cv2.imread("images/eun.jpg")
cv2.imshow('original', image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale', gray)
gray2 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow('grayscale2', gray2)
cv2.waitKey(0)


# 파일 저장
# jpg 형식
cv2.imwrite('images/grayeun.jpg', gray2)
# png 형식
#cv2.imwrite('images/grayeun.png', gray2)

cv2.destroyAllWindows()