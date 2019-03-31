import numpy as np
import cv2
import os
from sklearn.model_selection import train_test_split
import keras

class_names = ["wader", "Sea_bird", "Natatores"]

def load_img_data_to_array(img_dir, norm_size):
    jpg_num = 0
    for i in range(len(class_names)):
        dir = img_dir + class_names[i]
        ls_data = os.listdir(dir)
        jpg_num += len(ls_data)
    data_array = np.zeros((jpg_num, norm_size, norm_size, 3)) # RGB为三通道

    k=0
    class_label = []
    for i in range(len(class_names)):
        dir = img_dir + class_names[i]
        ls_data = os.listdir(dir)
        for j in range(len(ls_data)):
            img_path = os.path.join(dir, ls_data[j])
            img = cv2.imread(img_path)
            #img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            img_norm = cv2.resize(img,(norm_size, norm_size))  #in this project, norm_size = 140
            data_array[k] = np.array(img_norm)
            class_label.append(class_names[i])
            k += 1
    label_array = np.array(class_label)
    return data_array, label_array


def export_array(img_dir, norm_size):
    data_array = load_img_data_to_array(img_dir, norm_size)
    data_array.tofile("img_array.dat", sep=",", format='%d')
    pass

def split_dataset(data_array, label_array):
    train_X, test_X, train_y, test_y = train_test_split(data_array, label_array, test_size=0.2, random_state=2)
    return train_X, test_X, train_y, test_y

if __name__ == '__main__':
    img_dir = "C:/Users/Shangjie Zou/PycharmProjects/CV_bird/imgs/"
    norm_size = 140
    data_array = load_img_data_to_array(img_dir, norm_size)[0]
    label_array = load_img_data_to_array(img_dir, norm_size)[1]
    print("number of trainning set:" + str(len(split_dataset(data_array, label_array)[0])))
    print("number of test set:" + str(len(split_dataset(data_array, label_array)[1])))


