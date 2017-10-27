from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import imutils
import cv2
import os

path = os.getcwd() + os.sep
path_pedestre = path + '../db_aulas/Imagens/minibases/pedestres'

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

print(path)
print(__file__)

# haarcascade
# body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# loop over the image paths
imagePaths = list(paths.list_images(path_pedestre))

for imagePath in imagePaths:
# load the image and resize it to (1) reduce detection time
# and (2) improve detection accuracy
    image = cv2.imread(imagePath, 0)
    image = imutils.resize(image, width=min(400, image.shape[1]))
    orig = image.copy()

# detect people in the image
    (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
                                            padding=(8, 8), scale=1.05)
#   rects = body_classifier.detectMultiScale(image, 1.1, 5)

# draw the original bounding boxes
    for (x, y, w, h) in rects:
            cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

# apply non-maxima suppression to the bounding boxes using a
# fairly large overlap threshold to try to maintain overlapping
# boxes that are still people
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

# draw the final bounding boxes
    for (xA, yA, xB, yB) in pick:
            cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

# show some information on the number of bounding boxes
    filename = imagePath[imagePath.rfind("/") + 1:]
# print("[INFO] {}: {} original boxes, {} after suppression".format(
# 	filename, len(rects), len(pick)))
    print("[INFO] %s: %d original boxes, %d after suppression" %(
            filename, len(rects), len(pick)))

# show the output images
    cv2.imshow("Before NMS", orig)
    cv2.imshow("After NMS", image)
    cv2.waitKey(0)

