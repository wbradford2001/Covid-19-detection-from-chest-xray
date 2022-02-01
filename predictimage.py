import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Input, Conv2D, Dense, Flatten, Dropout, MaxPool2D
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Model
from glob import glob
from PIL import Image
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator


import pydicom

import cv2
import skimage

input_layer = Input(shape = (400,400,3))
conv1 = Conv2D(32, (3,3), strides = 2, activation = 'relu')(input_layer)
maxpool1 = MaxPool2D(2,2)(conv1)
conv2 = Conv2D(64, (3,3), strides = 2, activation = 'relu')(maxpool1)
maxpool2 = MaxPool2D(pool_size = (2, 2))(conv2)
flat1 = Flatten()(maxpool2)
dense1 = Dense(256, activation = 'relu')(flat1)
output_layer = Dense(1, activation = 'sigmoid')(dense1)
model = Model(input_layer, output_layer)

#compiling the CNN model
model.load_weights('./weights')

#single_image_path = '/Users/sipebradford/Downloads/SAMPLE DICOM FILES/single files/image-00000.dcm'
def predict_image(file_path):
    try:
        img = pydicom.dcmread(file_path).pixel_array
    ##    plt.imshow(img)
    ##    plt.show()    
        img_tensor = cv2.resize(img, dsize=(400, 400), interpolation=cv2.INTER_CUBIC)
        img_tensor = skimage.color.gray2rgb(img_tensor)
        img_tensor = np.expand_dims(img_tensor, axis = 0)

        pred = model.predict(img_tensor)
        if pred == 0:
            return 'Normal'
        elif pred == 1:
            return 'Pneumonia/COVID-19'
    except Exception as e:

        return("Unable to read DICOM File: " + str(e))


    
