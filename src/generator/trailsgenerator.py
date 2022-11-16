import numpy as np
import matplotlib.pyplot as plt 
import cv2 as cv
import glob
import pathlib
import os


class TrailsGenerator():
    def __init__(self, sequence_repository:str, generated_img_name :str, generated_img_extension : str):
        self.sequence_repository = sequence_repository
        self.generated_img_name = generated_img_name
        self.generated_img_extension = generated_img_extension
        assert self.generated_img_extension in ["jpg", "jpeg", "png"], "Please choose a valid image extension among ['jpg', 'jpeg', 'png'] "

        self.parent_path = pathlib.Path(os.path.realpath(__file__)).parent.parent.parent
        print(self.parent_path)
        for img in glob.glob(f"{self.sequence_repository}/*"):
            self.shape = cv.imread(img).shape
            break
        print(self.parent_path)
        
    def generate_trails(self):
        img_result = np.zeros(self.shape, dtype="uint8")

        for img in glob.glob(f"{self.sequence_repository}/*"):
          img = cv.cvtColor(cv.imread(img), cv.COLOR_BGR2RGB)

          img_result = np.maximum(img, img_result)
          del img
        
        cv.imwrite(f"{self.parent_path}/data/generated/{self.generated_img_name}.{self.generated_img_extension}", img_result)
        return img_result