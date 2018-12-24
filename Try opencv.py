import numpy as np
import cv2

# open image
if(0):
    img = cv2.imread("Kingfisher.jpg")  # Read Image
    cv2.namedWindow("kingfisher")       # name the window
    cv2.imshow("Kingfisher",img)        # command to show the image
    cv2.waitKey(0)                      # control the time for showing the img

    cv2.destroyAllWindows()

    print img.shape



# Change the image to single-tunnel picture
def Pic_Change(Picture):
    Picture = cv2.cvtColor(Picture,cv2.COLOR_BGR2GRAY)  # change to gray (single_tunnel)
    Picture = cv2.resize(Picture,(200,200))             # resize pixel data to 200*200
    list_pict = []
    for i in range(200):
        for j in range(200):
            pixel = float(Picture[i][j])/255.0   # see explanation on https://www.imooc.com/article/23430?block_id=tuijian_wz
            list_pict.append(pixel)

    arr_pict = np.array(list_pict)
    return arr_pict


Picture = cv2.imread("Kingfisher.jpg")
arr_pict = Pic_Change(Picture)
print arr_pict

