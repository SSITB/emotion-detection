import numpy as np
from keras.utils.np_utils import to_categorical
from keras.preprocessing.image import img_to_array
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import glob
import cv2
import os



def read_images(path):
    return [cv2.imread(img) for img in glob.glob(path)]



def convert_rgb(images):
    return [img[:, :, ::-1] for img in images if img is not None]



def resize_images(images):
    return [cv2.resize(img, (50, 50)) for img in images]



def detect_and_crop(images):
    face_detector = cv2.CascadeClassifier('./default.xml')
    new = []
    for img in images:
        pix = face_detector.detectMultiScale(img, 1.4, minNeighbors=1, minSize=(1,1))
        if len(pix) == 1:
            for (x,y,w,h) in pix:
                x = x
                y = y
                w = w
                h = h
            face = img[y:(y + h), x:(x + w)]
        elif len(pix) == 0:
            pix = face_detector.detectMultiScale(img, 1.2, minNeighbors=1, minSize=(1,1))
            for (x,y,w,h) in pix:
                x = x
                y = y
                w = w
                h = h
            face = img[y:(y + h), x:(x + w)]
        elif len(pix) > 1:
            pix = face_detector.detectMultiScale(img, 1.8, minNeighbors=1, minSize=(1,1))
            for (x,y,w,h) in pix:
                x = x
                y = y
                w = w
                h = h
            face = img[y:(y + h), x:(x + w)]
        new.append(face)
    return new



def plot_images(images, n1, n2):
    fig, (ax1, ax2) = plt.subplots(ncols=2)
    ax1.imshow(images[n1])
    ax2.imshow(images[n2]);



def write_images(images, folder):
    total = 0
    for img in images:
        path = os.path.sep.join([folder, f'{str(total).zfill(4)}.jpeg'])
        cv2.imwrite(path, img)
        total += 1


def test_image(path):
    print('Reading the image')
    rand_img = cv2.imread(path)
    print('Resizing the image and making predictions')
    rand_img = cv2.resize(rand_img.copy(), (50,50), 3)
    rand_img = rand_img.astype('float32') / 255.0
    rand_img = rand_img.reshape(-1, 50, 50, 3)
    prediction = model.predict_classes(rand_img)
    label = class_labels[prediction[0]]
    print('Drawing the label')
    test_img = Image.open(path)
    font = ImageFont.truetype('Arial.ttf', size=25)
    draw = ImageDraw.Draw(test_img).text((30,30), label, (0,0,0), font=font)
    print('Here\'s what model predicted:')
    plt.imshow(test_img);
