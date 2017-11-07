import matplotlib.pyplot as plt
import numpy as np
import cv2

face_xml_path = 'haarcascade_frontalface_default.xml'

face_cascade = cv2.CascadeClassifier(face_xml_path)

target_size = (128, 128)

def convertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def faceRetriever(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.imshow(gray, cmap='gray')

    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    result = []
    for (x,y,w,h) in faces:
        crop_img = cv2.resize(img[y:y+h, x:x+w], target_size)
        result.append((crop_img, (x,y,w,h)))

    return result