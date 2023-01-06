import cv2


def has_face(photo):
    # Load the photo using OpenCV
    image = cv2.imdecode(photo, cv2.IMREAD_COLOR)

    # Load the Haar cascade for detecting faces
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # Detect faces in the photo
    faces = cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)

    # Return True if a face was detected, False otherwise
    return len(faces) > 0
