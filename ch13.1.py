import cv2.cv2 as cv

# read image files
img1 = cv.imread('./imagedata/image1.png')
img1 = cv.resize(img1, (600, 400))
img2 = cv.imread('./imagedata/image2.png')
img2 = cv.resize(img2, (600, 400))
# use ORB
detector = cv.ORB_create()
# matching images
kp1, des1 = detector.detectAndCompute(img1, None)
kp2, des2 = detector.detectAndCompute(img2, None)
bf = cv.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# matching list
matched = []
for match1, match2 in matches:
    ratio = match1.distance/match2.distance
    if ratio < 0.8:
        matched.append([match1])

 # return result
imgmatches = cv.drawMatchesKnn(img1, kp1, img2, kp2, matched, None, flags=2)
cv.imshow("image matching", imgmatches)

cv.waitKey(0)
cv.destroyAllWindows()
