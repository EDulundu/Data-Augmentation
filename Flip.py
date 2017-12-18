import cv2

train_fd = open("/home/emre/Desktop/train.txt", "r")

index = 501

TRAIN_PATH = "/home/emre/Desktop/data/train/SCUT-FBP-"

list = []

for i in range(400):

    token = train_fd.readline()

    full_path = token.split()[0]

    label = token.split()[1]

    image = cv2.imread(full_path, cv2.IMREAD_COLOR)

    flipped = cv2.flip(image, 1)

    cv2.imwrite("/home/emre/Desktop/data/flip/SCUT-FBP-" + str(index) + ".jpg", flipped)

    list.append(TRAIN_PATH + str(index) + ".jpg" + " " + label)

    index += 1

    print i, "islendi"

train_fd.close()

train_fd = open("/home/emre/Desktop/train.txt", "a")

for i in range(400):
    train_fd.write(list[i] + "\n")

train_fd.close()