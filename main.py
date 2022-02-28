print("Loading Required Libraries....")
import predictimage
import os
from glob import glob


while True:
    print("\nEnter File Path To Directory or DICOM file:\n")
    filepath = input()
    print()
    if os.path.isdir(filepath)== False:
        print( os.path.basename(filepath) + ": " + predictimage.predict_image(filepath))
    else:
        filepaths = (glob(filepath + '/*')) 
        for path in sorted(filepaths):
            #print(path)
            #print(predictimage.predict_image(path))
            print(str(os.path.basename(path)) + ": " + str(predictimage.predict_image(path)))
            #print( os.path.basename(path) + ": " + predictimage.predict_image(path))
