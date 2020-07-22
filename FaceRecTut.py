import cv2
from random import randrange

# load some trained face data on the face fronmtals from opencv haar cascade algoithm
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# chose image to detect faces in
# img = cv2.imread('RDJ.jpg')
img = cv2.imread('rockers.jpg')
# webcam = cv2.VideoCapture(0)
'''
# iteraate forever over frames
while True: 
    # read the current frame
    successful_frame_read, frame = webcam.read()

    # must convert to greyscale
    greyscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)

    # draw rectangle around the face
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 256, 0))

    cv2.imshow('Saka Face Detector', frame)
    key = cv2.waitKey(1)

    # stop if Q or q is pressed
    if key==81 or key==113:
        break

# realease the video capture onject

webcam.release()
'''


# must convert to greyscale
greyscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect faces
face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)

# draw rectangle around the face
# (x, y, w, h) = face_coordinates[0]
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 10)

# print(face_coordinates)

cv2.imshow('Saka Face Detector', img)
cv2.waitKey()

print('code complete')
