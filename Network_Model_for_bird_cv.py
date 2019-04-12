import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Activation, Flatten
from keras import optimizers
from keras.metrics import categorical_accuracy
import matplotlib.pyplot as plt


Epochs = 10
Batch_size = 40
Initial_learningRate = 0.001
norm_size = 32
#data_array = np.fromfile("data_array.dat", sep=',').reshape((241, 140, 140, 3))
#label_array = np.fromfile("label_array.dat", sep=',').reshape((241,))
train_X = np.fromfile("train_X.dat", sep=',').reshape((192, norm_size, norm_size, 3))
test_X = np.fromfile("test_X.dat", sep=',').reshape((48, norm_size, norm_size, 3))
train_Y = np.fromfile("train_Y.dat", sep=',').reshape((192,))
test_Y = np.fromfile("test_Y.dat", sep=',').reshape((48,))



def build_model(width, height, depth, classes):
    model = Sequential()
    model.add(Conv2D(filters=6,kernel_size=5, strides=1,padding="same",
                     input_shape=(width,height,depth)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

    model.add(Conv2D(filters=16,kernel_size=5, strides=1,padding="same"))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

    model.add(Flatten())
    model.add(Dense(units=120, activation="relu"))
    model.add(Dense(units = 84, activation='relu'))

    #output
    model.add(Dense(units=classes, activation="softmax"))
    return model

if __name__ == '__main__':
    model = build_model(width=norm_size, height = norm_size, depth = 3, classes=3)
    opt = optimizers.Adam(lr=Initial_learningRate, decay=Initial_learningRate/Epochs)   # 学习率衰减
    model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])   # ["accuracy"]

    trained_model = model.fit(train_X, train_Y, epochs = Epochs, batch_size = Batch_size)
    y_predict = trained_model.predict(test_X)

    plt.style.use('ggplot')
    N = Epochs
    plt.plot(np.arange(0,N), trained_model.history['loss'], label = "train_loss")
    plt.plot(np.arange(0, N), trained_model.history["val_loss"], label="val_loss")
    plt.plot(np.arange(0, N), trained_model.history["acc"], label="train_acc")
    plt.plot(np.arange(0, N), trained_model.history["val_acc"], label="val_acc")
    plt.title("Training Loss and Accuracy on traffic-sign classifier")
    plt.xlabel("Epoch #")

    plt.ylabel("Loss/Accuracy")

    plt.legend(loc="lower left")

    score = model.evaluate(test_X, test_Y, batch_size = 48)
    accuracy = categorical_accuracy(test_Y, y_predict)
    print("score on test set:")
    print(score)
    print("categorical_accuracy:")
    print(accuracy)
