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
train_data_generator= ImageDataGenerator(rescale = 1./255,
                                        shear_range = 0.2,
                                        zoom_range = 0.2,
                                        horizontal_flip = True)

import pydicom
import scipy
import cv2
import skimage

training_data_path = '/Users/sipebradford/Downloads/xray_dataset_covid19/train'
test_data_path = '/Users/sipebradford/Downloads/xray_dataset_covid19/test'

output_classes = len(glob(training_data_path + '/*'))
#print('Number of output classes is: ', output_classes)

training_files = glob(training_data_path + '/*/*')
test_files = glob(test_data_path + '/*/*')
#print(len(training_files))
#print(len(test_files))

test_image = Image.open(training_files[0])
test_image = test_image.resize((400,400))

##plt.imshow(test_image)
##plt.show()

test_data_generator = ImageDataGenerator(rescale = 1./255)

training_data = train_data_generator.flow_from_directory(training_data_path, target_size = (400,400), batch_size = 4, class_mode = 'binary')

test_data = train_data_generator.flow_from_directory(test_data_path, target_size = (400,400), batch_size = 4, class_mode = 'binary')
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
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
model_history = model.fit(training_data, epochs = 12, validation_data = test_data, verbose = 1)
model.save_weights('./weights')

    
