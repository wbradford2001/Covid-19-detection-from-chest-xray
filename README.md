# Covid-19-detection-from-chest-xray

Upload DICOM files(specifically X-rays of the chest area) and detect whether or not the subject in them has COVID-19 induced pneumonia

Data Set was provided by Wei Hao Khoong at https://www.kaggle.com/khoongweihao/covid19-xray-dataset-train-test-sets

# Introduction
This is a simple program that, through a Convolutional Neural Network, outputs whether or not an X-ray is of a patient with COVID-19 induced pneumonia or not. The convenienve in this program vs others is that isntead of uploading images, the images are extracted from DICOM files directly, so users only need to obtain the DICOM file of whatever patient they want to test and upload the file path to it.

# Description
"ModelTrainer.py" is the script used to actually train the model. The model itself is the "finalized_model.sav" and is a pickled object. "PredictImage.py" is the script where it defines the function that takes user input and outputs the result. "Main.py" is what puts it all together and runs "predict_image" from "PredictImage.py". 

# Instructions
See Docker Repository: https://hub.docker.com/repository/docker/wjbradfo/covid19fromxray
Run as a docker container you be prompted to enter the path to your DICOM file(s).




# References
[1] Joseph Paul Cohen and Paul Morrison and Lan Dao. COVID-19 image data collection, arXiv, 2020. https://github.com/ieee8023/covid-chestxray-dataset