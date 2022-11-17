import numpy as np
import matplotlib.pyplot as plt 
import cv2 as cv
import glob
import pathlib
import os
from tqdm import tqdm
from ..tests import Tester

class TrailsGenerator():
  """
    A class used to represent the star trails generator
    .. 

    Attributes
    ----------

    sequence_repository : str
        the image sequence repository (please be sure that your images have the same shape) 

    generated_img_name : str
        the name of your generated image (star trailed image) 

    generated_img_extension : str
        the extension of your generated image (either "JPG", "JPEG" or "PNG") 

    generated_img_repository : str, default = None
        here you specify where you want to save your generated trailed image. By default, the generated image is stored in the sequence repository 

    Methods
    -------
    generate_trails()
        Automatically loads the image sequence and generate a star trailed image.
  """
    
  def __init__(self, sequence_repository:str, generated_img_name :str, generated_img_extension : str, generated_img_repository :str = None):
      self.sequence_repository = sequence_repository
      self.generated_img_name = generated_img_name
      self.generated_img_extension = generated_img_extension
      self.generated_img_repository = generated_img_repository
      self.generated_img_repository = self.sequence_repository if self.generated_img_repository is None else self.generated_img_repository

      # Assert if the sequence repository is valid
      tester = Tester()
      tester.check_a_directory(repository=self.sequence_repository)
      tester.check_if_a_directory_is_empty(repository=self.sequence_repository)
      tester.check_if_a_directory_contains_images(repository=self.sequence_repository)

      # Assert if the generated image repository is also valid
      tester.check_a_directory(repository=self.generated_img_repository)

      # Assert if the generated image extension is valid
      tester.check_generated_img_extension(generated_img_extension=self.generated_img_extension)

      #self.parent_path = pathlib.Path(os.path.realpath(__file__)).parent.parent.parent

      for img in glob.glob(f"{self.sequence_repository}/*"):
          self.shape = cv.imread(img).shape
          break
        
  def generate_trails(self):
      """
      Automatically loads the image sequence and generate a star trailed image. 

      Parameters
      ----------
      
      Returns
      -------
      img_result : ndarray of the same image sequence shape.
          Generated trailed image.

      Notes
      -----
      This method saves the generated image in the specified generated_img_repository or by default in the sequence repository.
      
      """
      img_result = np.zeros(self.shape, dtype="uint8")

      for img in tqdm(glob.glob(f"{self.sequence_repository}/*")):
        img = cv.cvtColor(cv.imread(img), cv.COLOR_BGR2RGB)
        img_result = np.maximum(img, img_result)

        # for each iteration delete the intermediate img from RAM to avoid filling it up. 
        del img
      
      #cv.imwrite(f"{self.parent_path}/data/generated/{self.generated_img_name}.{self.generated_img_extension}", cv.cvtColor(img_result, cv.COLOR_BGR2RGB))
      cv.imwrite(f"{self.generated_img_repository}/{self.generated_img_name}.{self.generated_img_extension}", cv.cvtColor(img_result, cv.COLOR_BGR2RGB))
      return img_result