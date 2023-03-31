import tensorflow as tf
import numpy as np
import json
import os
import time
import cv2
import serial
from PIL import Image
import threading

print("Start")
port = "COM16"
bluetooth=serial.Serial(port,9600)
print("Connected")

def pre_process(img):
    img = tf.keras.preprocessing.image.load_img(img, target_size=(96, 96))
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return img

model = tf.keras.models.load_model("mobilenet_finetune.h5")
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    cv2.imwrite("frame.jpg",frame)

    pred_img = pre_process("frame.jpg")
    pred = int(tf.round(tf.nn.sigmoid(model.predict(pred_img))));

    if pred == 0:
        print("Your Waste is Bio-Degradable!")
        bluetooth.flushInput()
        bluetooth.write(b"1")
        time.sleep(5)
        # time.sleep(0.1)
        print("Done")

    else:
        print("Your Waste is Non-Biodegradable!")

    os.remove("frame.jpg")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

bluetooth.close()
cap.release()
cv2.destroyAllWindows()