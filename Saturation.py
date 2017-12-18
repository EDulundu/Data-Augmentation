import cv2
import numpy as np

DATASET_PATH = "/home/emre/Desktop/Data_Set/train_set/SCUT-FBP-"
LABEL_PATH = "/home/emre/Desktop/Rating_Collection/labels.txt"

train_fd = open("/home/emre/Desktop/train.txt", "r")

index = 4901

list = []


for k in range(2400):

    token = train_fd.readline()

    path = token.split()[0]
    label = token.split()[1]

    image = cv2.imread(path, cv2.IMREAD_COLOR)

    hls_image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

    saturation = np.array(hls_image[:, :, 2], dtype=int)

    saturation /= 2

    # saturation[np.where(saturation >= 255)] = 255

    hls_image[:,:,2] = saturation

    rgb = cv2.cvtColor(hls_image, cv2.COLOR_HLS2BGR)

    cv2.imwrite("/home/emre/Desktop/data/saturationbol/SCUT-FBP-" + str(index) + ".jpg", rgb)

    list.append("/home/emre/Desktop/data/train/SCUT-FBP-" + str(index) + ".jpg" + " " + label)

    index += 1

    print k, "islendi"

train_fd.close()

train_fd = open("/home/emre/Desktop/train.txt", "a")

for i in range(2400):
    train_fd.write(list[i] + "\n")

train_fd.close()