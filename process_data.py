import numpy as np
import cv2
import os
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import img_to_array


class_names = ["wader", "Sea_bird", "Natatores"]

def load_img_data_to_array(img_dir, norm_size):
    jpg_num = 0
    for i in range(len(class_names)):
        dir = img_dir + class_names[i]
        ls_data = os.listdir(dir)
        jpg_num += len(ls_data)

    #k=0
    data_matrix = []
    class_label = []
    for i in range(len(class_names)):
        dir = img_dir + class_names[i]
        ls_data = os.listdir(dir)
        for j in range(len(ls_data)):
            img_path = os.path.join(dir, ls_data[j])
            img = cv2.imread(img_path)
            #img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            img_norm = cv2.resize(img,(norm_size, norm_size))  #in this project, norm_size = 140
            image = img_to_array(img_norm)
            data_matrix.append(image)
            if class_names[i] == "wader":
                class_label.append(0)
            elif class_names[i] == "Sea_bird":
                class_label.append(1)
            elif class_names[i] == "Natatores":
                class_label.append(2)

    label_array = np.array(class_label)
    data_array = np.array(data_matrix, dtype="float")
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
    norm_size = 32
    data_array = load_img_data_to_array(img_dir, norm_size)[0]
    label_array = load_img_data_to_array(img_dir, norm_size)[1]
    print("number of trainning set:" + str(len(split_dataset(data_array, label_array)[0])))
    print("number of test set:" + str(len(split_dataset(data_array, label_array)[1])))
    print("data_array.shape:")
    print(data_array.shape)
    print("label_array.shape")
    print(label_array.shape)
    do_what = input("Output dataset arrays to file?(N/Y):")
    if do_what == "Y":
        data_array.tofile("data_array.dat", sep=',')
        label_array.tofile("label_array.dat", sep=',')
    else:
        print("No output of arrays")

    train_X = split_dataset(data_array, label_array)[0]
    test_X = split_dataset(data_array, label_array)[1]
    train_Y = split_dataset(data_array, label_array)[2]
    test_Y = split_dataset(data_array, label_array)[3]
    print('train_Y:')
    print(train_Y)
    print('test_Y:')
    print(test_Y)
    switch_what = input("Output training and testset arrays to file?(N/Y):")
    if switch_what == "Y":
        train_X.tofile("train_X.dat", sep=',')
        test_X.tofile("test_X.dat", sep=',')
        train_Y.tofile("train_Y.dat", sep=',')
        test_Y.tofile("test_Y.dat", sep=',')
    else:
        print("No output of arrays")
