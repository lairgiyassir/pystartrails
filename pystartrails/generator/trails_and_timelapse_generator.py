import numpy as np
import cv2
import os
import glob
from tqdm import tqdm
from ..tests import Tester
from concurrent.futures import ThreadPoolExecutor


class TrailsAndTimeLapseGenerator:
    """
    A class used to generate star trails and create time-lapse videos.

    Attributes
    ----------
    sequence_repository : str
        The image sequence repository (please ensure that your images have the same shape).

    generated_img_name : str
        The name of your generated image (star-trailed image).

    generated_img_extension : str
        The extension of your generated image (either "JPG", "JPEG" or "PNG").

    generated_img_repository : str, default = None
        Specifies where you want to save your generated trailed image. By default, the generated image is stored in the sequence repository.

    output_extension : str, default = 'mp4'
        The extension of the output time-lapse video (e.g., 'mp4', 'avi').

    fps : int, default = 10
        Frames per second for the time-lapse video.

    Methods
    -------
    generate_trails()
        Automatically loads the image sequence and generates a star-trailed image.

    create_timelapse(output_filename='timelapse')
        Creates a time-lapse video from the list of images in the sequence repository.
    
    create_blended_timelapse(output_filename='blended_timelapse')
        Creates a blended time-lapse video from the list of images in the sequence repository.
    """
    
    def __init__(self, sequence_repository: str, generated_img_name: str, generated_img_extension: str, generated_img_repository: str = None, output_extension='mp4', fps=10):
        self.sequence_repository = sequence_repository
        self.generated_img_name = generated_img_name
        self.generated_img_extension = generated_img_extension
        self.generated_img_repository = sequence_repository if generated_img_repository is None else generated_img_repository
        self.output_extension = output_extension
        self.fps = fps
        self.fourcc = cv2.VideoWriter_fourcc(*'mp4v') if output_extension == 'mp4' else cv2.VideoWriter_fourcc(*'XVID')
        self.image_list = self._get_image_list()
        
        # Assert the validity of the sequence and generated image repository
        tester = Tester()
        tester.check_a_directory(repository=self.sequence_repository)
        tester.check_if_a_directory_is_empty(repository=self.sequence_repository)
        #tester.check_if_a_directory_contains_images(repository=self.sequence_repository)
        tester.check_a_directory(repository=self.generated_img_repository)
        tester.check_generated_img_extension(generated_img_extension=self.generated_img_extension)
        tester.check_image_consistency(repository=self.sequence_repository)
        tester.check_fps_validity(fps=self.fps)

        # Get image shape from the first image
        for img in glob.glob(f"{self.sequence_repository}/*"):
            self.shape = cv2.imread(img).shape
            break
    
    def _get_image_list(self):
        """
        Get the sorted list of image file paths from the images directory.
        
        :return: Sorted list of image file paths.
        """
        files = os.listdir(self.sequence_repository)
        images = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
        images.sort()
        return [os.path.join(self.sequence_repository, img) for img in images]
    
    def adjust_color_temperature_and_tint(self, image):
        """
        Adjusts the color temperature and tint of the input image.

        Parameters
        ----------
        image : ndarray
            Input image.

        Returns
        -------
        image : ndarray
            Image with adjusted color temperature and tint.
        """
        # Adjust color temperature
        image = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)
        l, a, b = cv2.split(image)
        
        b = cv2.add(b, int((self.color_temperature - 1) * 128))
        a = cv2.add(a, int(self.tint * 128))
        
        image = cv2.merge([l, a, b])
        image = cv2.cvtColor(image, cv2.COLOR_LAB2RGB)
        
        return image

    def apply_noise_reduction(self, image):
        """
        Applies noise reduction to the input image.

        Parameters
        ----------
        image : ndarray
            Input image.

        Returns
        -------
        image : ndarray
            Denoised image.
        """
        if self.noise_reduction_strength > 0:
            image = cv2.fastNlMeansDenoisingColored(image, None, self.noise_reduction_strength, self.noise_reduction_strength, 7, 21)
        return image

    def generate_trails(self, n_images=None):
        """
        Automatically loads the image sequence and generates a star-trailed image 
        by processing one image out of every `step` images.

        Parameters
        ----------
        n_images : int, optional
            Number of images to use (default is All).

        Returns
        -------
        img_result : ndarray
            Generated trailed image.
        """

        img_result = np.zeros(self.shape, dtype="uint8")

        # Retrieve and sort image paths for consistent ordering
        image_paths = sorted(glob.glob(f"{self.sequence_repository}/*"))

        # Process every `step`-th image
        if n_images is not None:
            step = len(self.image_list) // n_images
    
        for img_path in tqdm(image_paths[::step]):
            img = cv2.imread(img_path)
            if img is None:
                continue  # Skip if the image couldn't be loaded
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_result = np.maximum(img, img_result)

        output_path = f"{self.generated_img_repository}/{self.generated_img_name}.{self.generated_img_extension}"
        cv2.imwrite(output_path, cv2.cvtColor(img_result, cv2.COLOR_BGR2RGB))
        return img_result

    def create_timelapse(self, blended_timelapse = True, output_filename='timelapse'):
        """
        Create the time-lapse video from the list of images.
        
        :param output_filename: The name of the output video file (without extension).
        """
        
        height, width, _ = self.shape
        output_file = f"{output_filename}.{self.output_extension}"
        out = cv2.VideoWriter(output_file, self.fourcc, self.fps, (width, height))
        img_result = np.zeros(self.shape, dtype="uint8")
        
        
        for image_path in tqdm(self.image_list):
            current_image = cv2.imread(image_path)
            #current_image = cv2.cvtColor(current_image, cv2.COLOR_BGR2RGB)
            
            if blended_timelapse:
                img_result = np.maximum(current_image, img_result)
                #out.write(cv2.cvtColor(img_result, cv2.COLOR_RGB2BGR))
                out.write(img_result)
            
            else:
                out.write(current_image)
        
        out.release()
        print(f"Timelapse video saved as {output_file}")
    
    def create_timelapse_parallel(self, blended_timelapse=True, output_filename='timelapse'):
        """
        Create the time-lapse video from the list of images.
        
        :param blended_timelapse: Whether to blend frames using the max operation.
        :param output_filename: The name of the output video file (without extension).
        """
        height, width, _ = self.shape
        output_file = f"{output_filename}.{self.output_extension}"
        out = cv2.VideoWriter(output_file, self.fourcc, self.fps, (width, height))
        
        # Initialize the blended image result.
        img_result = np.zeros(self.shape, dtype="uint8")
        
        # Function to read an image from disk.
        def read_img(path):
            return cv2.imread(path)
        
        # Use a thread pool to prefetch images.
        with ThreadPoolExecutor(max_workers=2) as executor:
            # Submit the first image.
            future = executor.submit(read_img, self.image_list[0])
            
            # Loop through the remaining images with a progress bar.
            for image_path in tqdm(self.image_list[1:], desc="Creating timelapse"):
                # Get the current image (this will wait if not already loaded).
                current_image = future.result()
                # Prefetch the next image.
                future = executor.submit(read_img, image_path)
                
                if blended_timelapse:
                    # Use cv2.max (implemented in C++) which can be faster than np.maximum.
                    img_result = cv2.max(current_image, img_result)
                    out.write(img_result)
                else:
                    out.write(current_image)
            
            # Process the last image.
            current_image = future.result()
            if blended_timelapse:
                img_result = cv2.max(current_image, img_result)
                out.write(img_result)
            else:
                out.write(current_image)
        
        out.release()
        print(f"Timelapse video saved as {output_file}")
