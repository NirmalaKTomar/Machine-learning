# -*- coding: utf-8 -*-
"""neural network Project:--**

Mnist digit recognition with Neural Netwoks

Tensorflow is used as the module that helps in building differnet neural networks.


---
"""

import tensorflow as tf
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

"""Example of an image in mnist dataset: """

import matplotlib.pyplot as plt
image_index = 7777 # You may select anything up to 60,000
print(y_train[image_index]) # The label is 8
plt.imshow(x_train[image_index], cmap='binary')

"""Reshaping the training and testing data in order to make it suitable as an input to the neural network

---


"""

# Reshaping the array to 4-dims so that it can work with the Keras API
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test1=x_test
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
input_shape = (28, 28, 1)

# Making sure that the values are float so that we can get decimal points after division
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Normalizing the RGB codes by dividing it to the max RGB value.
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print('Number of images in x_train', x_train.shape[0])
print('Number of images in x_test', x_test.shape[0])

"""Defining the neural networks with its layers using keras



---


"""

# Importing the required Keras modules containing model and layers
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
# Creating a Sequential Model and adding the layers
model = Sequential()
model.add(Conv2D(28, kernel_size=(3,3), input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten()) # Flattening the 2D arrays for fully connected layers
model.add(Dense(128, activation=tf.nn.relu))
model.add(Dropout(0.2))
model.add(Dense(10,activation=tf.nn.softmax))

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])
model.fit(x=x_train,y=y_train, epochs=10)

model.evaluate(x_test, y_test)

"""

---



Predicting the output for the test data and calculating the accuracy from scratch using for loop

The accuracy achieved is >98%

Hence the model is trained efficiently


---



---

"""

y_pred = model.predict_classes(x_test)

y_pred

import numpy as np
def plot(x,p,labels=False):
  plt.figure(figsize = (20,2))
  for i in range(10):
    plt.subplot(1,10,i+1)
    plt.imshow(x[i].reshape(28,28), cmap ='binary')
    if labels:
      plt.xlabel(p[i])
  plt.show()
plot(x_test1,y_pred,labels=True)

c=0
for i in range(10000):
  if(y_pred[i]!=y_test[i]):
    c+=1
print('Accuracy = ',(10000-c)/100)
