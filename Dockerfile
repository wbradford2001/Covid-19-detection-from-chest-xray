FROM python:latest


COPY . ./

RUN pip3 install numpy
RUN pip3 install --upgrade tensorflow
RUN pip3 install Pillow
RUN pip3 install scipy
RUN pip3 install opencv-python
RUN pip3 install pydicom
RUN pip3 install matplotlib
RUN pip3 install python-gdcm
RUN pip3 install pylibjpeg






CMD ["python", "main.py"]