import numpy as np
import cv2
import os


# open image
if(1):
    dir = "C:/Users/Shangjie Zou/PycharmProjects/CV_bird/imgs/Natatores/"
    ls_data = os.listdir(dir)
    for i in range(len(ls_data)):
        # 可以使用这个程序debug，找出数据集中无法被load的图片
        try:
            img_path = os.path.join(dir, ls_data[i])
            img = cv2.imread(img_path)  # Read Image
            img_array = np.array(img)
            #cv2.namedWindow("0")       # name the window
            #cv2.imshow("0",img)        # command to show the image
            #cv2.waitKey(0)                      # control the time for showing the img

            #cv2.destroyAllWindows()

            print (img.shape)
            #print(img_array.shape)
        except:
            print(ls_data[i])



# Change the image to single-tunnel picture
def Pic_Change(Picture):

    #Picture = cv2.cvtColor(Picture,cv2.COLOR_BGR2GRAY)  # change to gray (single_tunnel)
    Picture = cv2.resize(Picture,(140,140))             # resize pixel data to 200*200
    list_pict = []
    for i in range(16):
        for j in range(16):
            pixel = float(Picture[i][j])/255.0   # see explanation on https://www.imooc.com/article/23430?block_id=tuijian_wz
            list_pict.append(pixel)

    arr_pict = np.array(list_pict)
    return arr_pict,Picture


"""
dir = "C:/Users/Shangjie Zou/PycharmProjects/CV_bird/imgs/Sea_bird/0.jpg"
Picture = cv2.imread(dir)
arr_pict = Pic_Change(Picture)[0]
img = Pic_Change(Picture)[1]

cv2.namedWindow("gray")       # name the window
cv2.imshow("gray",img)        # command to show the image
cv2.waitKey(0)                      # control the time for showing the img
cv2.destroyAllWindows()
print(arr_pict)
"""
