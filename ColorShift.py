import cv2
import numpy as np
import Image

train_fd = open("/home/emre/Desktop/train.txt", "r")

index = 7301

list = []

for i in range(7200):

    token = train_fd.readline()

    path = token.split()[0]
    label = token.split()[1]

    image = cv2.imread(path, cv2.IMREAD_COLOR)

    b = image[:, :, 0]
    g = image[:, :, 1]
    r = image[:, :, 2]

    b = np.where(b + 5 < 5, 255, b + 5)
    # g = np.where(g + 20 < 20, 255, g + 20)
    r = np.where(r + 50 < 50, 255, r + 50)

    image[:, :, 0] = b
    image[:, :, 1] = g
    image[:, :, 2] = r

    cv2.imwrite("/home/emre/Desktop/data/shift/SCUT-FBP-" + str(index) + ".jpg", image)

    list.append("/home/emre/Desktop/data/train/SCUT-FBP-" + str(index) + ".jpg" + " " + label)

    index += 1

    print path, "islendi"

train_fd.close()

train_fd = open("/home/emre/Desktop/train.txt", "a")

for i in range(7200):
    train_fd.write(list[i] + "\n")

train_fd.close()