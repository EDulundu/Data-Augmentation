import cv2
import numpy as np

def image_resize(image, width = None, height = None, inter = cv2.INTER_CUBIC):

    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

# image = cv2.imread("/home/emre/Desktop/Data_Collection/SCUT-FBP-460.jpg", 1)
#
# my = image_resize(image, width=256)
#
# y, x, channel = my.shape
#
# new_image = np.zeros((256, 256, 3), dtype=np.uint8)
#
# a = int((256 - y)/2)
#
# new_image[a:y+a, :x, :channel] = my

# value = my[5, 5]
#
# for i in range(y, 256):
#     for j in range(256):
#         new_image[i, j] = value

# cv2.imwrite("/home/emre/Desktop/SCUT-FBP-460.jpg", new_image)


train_fd = open("/home/emre/Desktop/train.txt", "r")

for k in range(14400):

    token = train_fd.readline()

    path = token.split()[0]

    index = path.find("SCUT")
    name = path[index:]

    image = cv2.imread(path, cv2.IMREAD_COLOR)

    my_image = image_resize(image, height=256)

    y, x, channel = my_image.shape

    new_image = np.zeros((256, 256, 3), dtype=np.uint8)

    a = int((256 - x) / 2)

    if x != y:
        new_image[:y, a:x + a, :channel] = my_image
    else:
        new_image[:y, :x, :channel] = my_image

    cv2.imwrite("/home/emre/Desktop/train/" + name, new_image)

    print name, "islendi"

train_fd.close()
