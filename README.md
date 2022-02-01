# Covid-19-detection-from-chest-xray

Upload DICOM files(specifically X-rays of the chest area) and detect whether or not the subject in them has COVID-19 induced pneumonia

Data Set was provided by Wei Hao Khoong at https://www.kaggle.com/khoongweihao/covid19-xray-dataset-train-test-sets

# Introduction
This is a simple program that, through a Convolutional Neural Network, outputs whether or not an X-ray is of a patient with COVID-19 induced pneumonia or not. The convenienve in this program vs others is that isntead of uploading images, the images are extracted from DICOM files directly, so users only need to obtain the DICOM file of whatever patient they want to test and upload the file path to it.

# Description
"ModelTrainer.py" is the script used to actually train the model. The weights of the model are stored in "weights.dataweights.data-00000-of-00001". "PredictImage.py" is the script where it defines the function that takes user input and outputs the result. "Main.py" is what puts it all together and runs "predict_image" from "PredictImage.py". 

# Instructions
Simply run "main.py" and it will prompt you to enter a filepath to whatever DICOM files you wish to evaluate. You can also enter a filepath to a directory, and it will traverse the directory and wherever there are DICOM files, it will evaluate them for COVID-19 induced pneumonia. Have fun!




# References
[1] Joseph Paul Cohen and Paul Morrison and Lan Dao. COVID-19 image data collection, arXiv, 2020. https://github.com/ieee8023/covid-chestxray-dataset
