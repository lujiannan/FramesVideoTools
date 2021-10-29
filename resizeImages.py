# The program is used to edit the size of a set of images

import cv2
import os

def main():
    # the path of the source images
    data_path = "C:/Users/jlu2/Desktop/ComicRita/frames/"               # modify required
    # the path of output images
    output_path = "C:/Users/jlu2/Desktop/ComicRita/frames720p/"         # modify required
    # the size of the output images
    toSize = (720,720)                                                  # modify required
    # the number of images in the source path
    n = 192                                                             # modify required

    # if output path not existed, create one
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # resize the images one by one
    for i in range(n):
        # names of the source images
        imgName = "zjy (" + str(i + 1) + ").jpg"                        # modify required
        img_path = data_path + imgName
        img = cv2.imread(img_path,3)
        res = cv2.resize(img,toSize,interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(output_path + imgName,res)
        print(img_path)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()