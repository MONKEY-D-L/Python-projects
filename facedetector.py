import cv2
from random import randrange


trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# reading image
#img = cv2.imread('people.png')

# Using a webcam 
webcam = cv2.VideoCapture(0)
key = cv2.waitKey(1)

#iterate forever over frames
while True:
    successful_frame_read, frame = webcam.read()
    
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    
    for (x , y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+h, y+h), (randrange(128,256), randrange(128,256), randrange(128,256)), 2)
    
    cv2.imshow('Clever programmer face detector', frame)
    key = cv2.waitKey(1)
    
    if key==81 or key==113:
        break
    
webcam.release

"""""
#detect faces 
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)


#draw rectangles around the faces
for (x , y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+h, y+h), (randrange(128,256), randrange(128,256), randrange(128,256)), 2)

#print face coordinates
#print(face_coordinates)




#display image with face
cv2.imshow('Clever programmer face detector', img)
cv2.waitKey()
"""






print("code complete")
