import pathlib
from PIL import Image

class Tester:
    """
    A class used to represent the tester for the Trails and Time-lapse Generator.
    This class contains various checks to ensure the validity and integrity of the input data and parameters.

    Methods
    -------
    check_a_directory(repository: str)
        Checks if a directory exists.
    
    check_if_a_directory_is_empty(repository: str)
        Checks if a directory is empty.
    
    check_if_a_directory_contains_images(repository: str)
        Checks if a directory contains only valid image files (extensions: '.jpg', '.jpeg', '.png').
    
    check_generated_img_extension(generated_img_extension: str)
        Checks if the chosen generated image extension is valid.
    
    check_image_consistency(repository: str)
        Checks if all images in the directory have the same dimensions.
    
    check_fps_validity(fps: int)
        Checks if the frames per second (fps) value is valid and positive.
    """

    def __init__(self):
        pass

    def check_a_directory(self, repository: str):
        """
        This method checks if a repository exists.
        """
        assert pathlib.Path(repository).is_dir(), "Sequence repository is not found!"

    def check_if_a_directory_is_empty(self, repository: str):
        """
        This method checks if a repository is empty or not.
        """
        assert any(pathlib.Path(repository).iterdir()), "Sequence repository is empty!"

    def check_if_a_directory_contains_images(self, repository: str):
        """
        This method checks if a repository contains only valid image files (extensions: '.jpg', '.jpeg', '.png').
        """
        extensions_not_images = [path.suffix for path in pathlib.Path(repository).rglob("*") if path.suffix.lower() not in [".jpg", ".jpeg", ".png"]]
        assert len(extensions_not_images) == 0, "There are files that are not images in the repository! Please consider removing them before generating star trails."

    def check_generated_img_extension(self, generated_img_extension: str):
        """
        This method checks if the chosen generated image extension is valid.
        """
        assert generated_img_extension.lower() in ["jpg", "jpeg", "png"], "Please choose a valid image extension among ['jpg', 'jpeg', 'png']."

    def check_image_consistency(self, repository: str):
        """
        This method checks if all images in the directory have the same dimensions.
        SIMPLE FAST VERSION - best balance of speed and maintainability.
        """        
        # Fast file discovery
        image_paths = list(pathlib.Path(repository).rglob("*.[jJ][pP][gG]")) + \
              list(pathlib.Path(repository).rglob("*.[pP][nN][gG]"))
        
        if len(image_paths) < 2:
            raise ValueError("Not enough images to perform consistency check.")
        
        # Get reference size using PIL (much faster than cv2)
        with Image.open(image_paths[0]) as first_image:
            reference_size = first_image.size
        
        # Check remaining images
        for image_path in image_paths[1:]:
            with Image.open(image_path) as img:
                if img.size != reference_size:
                    raise AssertionError(f"Image dimensions mismatch found in {image_path}. All images must have the same dimensions.")

    def check_fps_validity(self, fps: int):
        """
        This method checks if the frames per second (fps) value is valid and positive.
        """
        assert isinstance(fps, int) and fps > 0, "FPS value must be a positive integer."

