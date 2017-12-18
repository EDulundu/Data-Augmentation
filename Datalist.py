import cv2

DATASET_PATH = "/home/emre/Desktop/Data_Collection/SCUT-FBP-"
LABEL_PATH = "/home/emre/Desktop/Rating_Collection/labels.txt"

TRAIN_LIST_PATH = "/home/emre/Desktop/train.txt"
VAL_LIST_PATH = "/home/emre/Desktop/val.txt"

train_fd = open(TRAIN_LIST_PATH, "w+")
val_fd = open(VAL_LIST_PATH, "w+")
label_fd = open(LABEL_PATH, "r")

count_4 = 15 # 4
count_3 = 30 # 6
count_2 = 175 # 43
count_1 = 179 # 46
count_0 = 1 # 1

TRAIN_PATH = "/home/emre/Desktop/data/train/SCUT-FBP-"
VAL_PATH = "/home/emre/Desktop/data/val/SCUT-FBP-"

for i in range(1, 501):

    label_token = label_fd.readline()

    label = int(label_token) - 1

    label_2 = str(label)

    image = cv2.imread(DATASET_PATH + str(i) + ".jpg", cv2.IMREAD_COLOR)

    if label == 4:
        if count_4 != 0:
            train_fd.write(TRAIN_PATH + str(i) + ".jpg" + " " + label_2 + "\n")
            cv2.imwrite(TRAIN_PATH + str(i) + ".jpg", image)
            count_4 -= 1
        else:
            val_fd.write(VAL_PATH + str(i) + ".jpg" + " " + label_2 + "\n")
            cv2.imwrite(VAL_PATH + str(i) + ".jpg", image)
    elif label == 3:
        if count_3 != 0:
            train_fd.write(TRAIN_PATH + str(i) + ".jpg" + " " + label_2 + "\n")
            cv2.imwrite(TRAIN_PATH + str(i) + ".jpg", image)
            count_3 -= 1
        else:
            val_fd.write(VAL_PATH + str(i) + ".jpg" + " " + label_2 + "\n")
            cv2.imwrite(VAL_PATH + str(i) + ".jpg", image)
    elif label == 2:
        if count_2 != 0:
            train_fd.write(TRAIN_PATH + str(i) + ".jpg" + " " + label_2 + "\n")
            cv2.imwrite(TRAIN_PATH + str(i) + ".jpg", image)
            count_2 -= 1
        else:
            val_fd.write(VAL_PATH + str(i) + ".jpg" + " " + label_2 + "\n")
            cv2.imwrite(VAL_PATH + str(i) + ".jpg", image)
    elif label == 1:
        if count_1 != 0:
            train_fd.write(TRAIN_PATH + str(i) + ".jpg" + " " + label_2 + "\n")
            cv2.imwrite(TRAIN_PATH + str(i) + ".jpg", image)
            count_1 -= 1
        else:
            val_fd.write(VAL_PATH + str(i) + ".jpg" + " " + label_2 + "\n")
            cv2.imwrite(VAL_PATH + str(i) + ".jpg", image)
    elif label == 0:
        if count_0 != 0:
            train_fd.write(TRAIN_PATH + str(i) + ".jpg" + " " + label_2 +"\n")
            cv2.imwrite(TRAIN_PATH + str(i) + ".jpg", image)
            count_0 -= 1
        else:
            val_fd.write(VAL_PATH + str(i) + ".jpg" + " " + label_2 + "\n")
            cv2.imwrite(VAL_PATH + str(i) + ".jpg", image)

    print i, "islendi"

label_fd.close()
train_fd.close()
val_fd.close()