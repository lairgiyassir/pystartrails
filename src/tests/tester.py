import pathlib 


class Tester():
    """
      A class used to represent the tester of the star trails generator
      ...

      Attributes
      ----------

      Methods
      -------
      check_a_directory(repository)

    """
    def __init__(self):
        pass

    def check_a_directory(self, repository:str):
        """
        This method checks if a repository exits.
        """
        assert pathlib.Path(repository).is_dir(), "Sequence repository is not found !"
    
    def check_if_a_directory_is_empty(self, repository:str):
        """
        This method checks if a repository is empty or not!
        """
        assert any(pathlib.Path(repository).iterdir()), "Sequence repository is empty !"
    
    def check_if_a_directory_contains_images(self, repository:str):
        """
        This method checks if a repository contains any non-image extensions (which are not ".jpg", ".jpeg", ".png").
        """
        existed_extensions_list = list(map( lambda x: x.suffix ,pathlib.Path(repository).rglob("*")))
        extensions_not_images = [element for element in existed_extensions_list if element.lower() not in [".jpg", ".jpeg", ".png"]]

        assert len(extensions_not_images) == 0, "There are files that are not images in the repository! Please consider removing them before generating star trails"

    def check_generated_img_extension(self, generated_img_extension:str):
        """
        This method checks if the chosen generated image extension is valid.
        """
        assert generated_img_extension.lower() in ["jpg", "jpeg", "png"], "Please choose a valid image extension among ['jpg', 'jpeg', 'png'] "

