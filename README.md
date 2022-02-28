# Covid-19-detection-from-chest-xray

Upload DICOM files(specifically X-rays of the chest area) and detect whether or not the subject in them has COVID-19 induced pneumonia

Data Set was provided by Wei Hao Khoong at https://www.kaggle.com/khoongweihao/covid19-xray-dataset-train-test-sets

# Introduction
This is a simple program that, through a Convolutional Neural Network, outputs whether or not an X-ray is of a patient with COVID-19 induced pneumonia or not with 93 percent accuracy. The convenienve in this program vs others is that isntead of uploading images, the images are extracted from DICOM files directly, so users only need to obtain the DICOM file of whatever patient they want to test and upload the file path to it.

# Description
"MODEL_CREATOR.ipynb" is the jupyter notebook used to actually create the model. The model itself is the "finalized_model.sav" and is a pickled object. "PredictImage.py" is the script where it defines the function that takes user input and outputs the result. "Main.py" is what puts it all together and runs "predict_image" from "PredictImage.py". 

# Instructions
## Method 1: Run using Conda Environment
- Step 1: Make sure git and anaconda(or mini conda) is installed on your machine
- Step 2: Initialize Git, clone repository, and enter Directory
```console
git init
git clone https://github.com/wbradford2001/Covid-19-detection-from-chest-xray
cd Covid-19-detection-from-chest-xray
```
- Step 3: build environment from "env.yml"
```console
conda env build --file env.yml --name environment_from_yml 
```
- Step 4: activate new environment
```console
conda activate environment_from_yml
```
- Step 5: If you want to see/manipulate how the model was created, open "MODEL_CREATOR.ipynb". If you just want the end product of being able to detect COVID-19, run "main.py"
```console
python3 main.py
```
And you will be prompted to enter a file path containing your DICOM files.

## Method 2: As a Docker Container
- Step 1: Make sure Docker is installed on your machine
- Step 2: Start the Docker Daemon
- Step 3: Pull down the Image from repository
  Docker Repository: https://hub.docker.com/repository/docker/wjbradfo/covid19fromxray
  ```console
  docker pull wjbradfo/covid19fromxray:1.0
  ```
- Step 4: Run as a container and enter interactive shell(-it)
  ```console
  docker run -it wjbradfo/covid19fromxray:1.0
  ````
  And you will be prompted to enter a file path containing your DICOM files.





# References
[1] Joseph Paul Cohen and Paul Morrison and Lan Dao. COVID-19 image data collection, arXiv, 2020. https://github.com/ieee8023/covid-chestxray-dataset
