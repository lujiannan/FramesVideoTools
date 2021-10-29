# The program is used to convert sets of images into videos

import cv2

def main():    
    # the path of source images
    data_path = "C:/Users/jlu2/Desktop/ComicRita/frames720p/"               # modify required
    # the path of output video
    output_path = "C:/Users/jlu2/Desktop/ComicRita/comic_8.mp4"             # modify required
    # the frame rate of the output video
    fps = 8                                                                 # modify required
    # the number of images in the source path
    n = 192                                                                 # modify required
    # obtain one image for height and width of the output video
    image = cv2.imread(data_path + "zjy (1).jpg")                           # modify required
    image_info = image.shape
    height = image_info[0]
    width = image_info[1]
    size = (height,width)
    print(size)

    """
    cv2.VideoWriter(param1, param2, param3, param4)
    param1: the path of output video
    param2: VideoWriter_fourcc is the video encoder/decoder
        fourcc is a Four-Character Codes，the following ones are commonly used
        cv2.VideoWriter_fourcc('I', '4', '2', '0'), YUV type        file postfix: .avi 
        cv2.VideoWriter_fourcc('P', 'I', 'M', 'I'), MPEG-1 type     file postfix: .avi 
        cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), MPEG-4 type     file postfix: .avi 
        cv2.VideoWriter_fourcc('T', 'H', 'E', 'O'), Ogg Vorbis type file postfix: .ogv 
        cv2.VideoWriter_fourcc('F', 'L', 'V', '1'), Flash type      file postfix: .flv
        cv2.VideoWriter_fourcc('M', 'P', '4', 'V'), mp4 type        file postfix: .mp4
    param3: frame rate, fps
    param4: (width,height), frame size of the output video
    """
    fourcc = cv2.VideoWriter_fourcc(*"MP4V")                                # modify required
    video = cv2.VideoWriter(output_path, fourcc, fps, (width,height))
    
    # write images to video one by one
    for i in range(n):
        # names of the source images
        imgName = "zjy (" + str(i + 1) + ").jpg"                            # modify required    
        image_path = data_path + imgName
        print(image_path)
        img = cv2.imread(image_path)
        video.write(img)
    
    video.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()