from scipy.misc import fromimage, toimage

import cv2
import Image, ImageEnhance
import numpy as np


def brightness_contrast(image, brightness = -100, contrast = 300):

    def vect(a):
        c   = contrast
        b   = brightness
        res = ((a - 128) * c + 128) + b
        if res < 0 :
            return 0
        if res > 255:
            return 255
        return res

    transform = np.vectorize(vect)
    data = transform(fromimage(image)).astype(np.uint8)
    return toimage(data)

train_fd = open("/home/emre/Desktop/contrast.txt", "r")

index = 1701

list = []

for i in range(800):

    token = train_fd.readline()

    path = token.split()[0]
    label = token.split()[1]

    image = Image.open(path)

    bright = brightness_contrast(image, brightness=0, contrast=1.5)

    bright.save("/home/emre/Desktop/data/contrast/SCUT-FBP-" + str(index) + ".jpg")

    list.append("/home/emre/Desktop/data/contrast/SCUT-FBP-" + str(index) + ".jpg" + " " + label)

    index += 1

    print path, "islendi"

train_fd.close()

train_fd = open("/home/emre/Desktop/contrast.txt", "a")

for i in range(800):
    train_fd.write(list[i] + "\n")

train_fd.close()