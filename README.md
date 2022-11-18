# PyStarTrails
Photographers and astrophotographers can use this package to quickly and easily generate star-trail images from a sequence of images in order to create stunning images of the night sky.

The previous image-processing software I used was Adobe Photoshop, a powerful image-processing program that can be used for the generation of star trails. However, I experienced slow computer performance after uploading a star trail image sequence (more than 500 images) since my RAM became overloaded with images. I was forced to divide the 500 images into small batches. This process took a considerable amount of time. 

Due to this, I have decided to develop a lightweight and fast program that does not require the installation of any external programs. I hope that this package will be useful for all astrophotographers and photographers worldwide :) 

Developed by [Yassir LAIRGI](https://lairgiyassir.github.io/) ©2022. 
# Installation
The PyStarTrails package can be installed through pip:

```bash
pip install pystartrails
```

# Usage
This package assumes that you have already a sequence of night sky images that you want to create a star-trail image based on. In order create your first star-trail image, specify : 

``` python
from pystartrails import TrailsGenerator

trails_generator = TrailsGenerator(sequence_repository, generated_img_repository, generated_img_extension, generated_img_name)
star_trail_img = trails_generator.generate_trails()
```
Where:

- sequence_repository (str) : the image sequence repository (please be sure that your images have the same shape).

- generated_img_name (str) : the name of your generated image (star trailed image) 

- generated_img_extension (str) : the extension of your generated image (either "JPG", "JPEG" or "PNG") 

- generated_img_repository (str) : here you specify where you want to save your generated trailed image. By default, the generated image is stored in the sequence repository

generate_trails() method returns array in the same format as the input format and in the same time saves the generated image in the specified generated_img_repository. 


# Example

This example is structured structured in three parts:

1. Prepare the folder of your night sky image sequence. This repository is actually the sequence_repository attribute of TrailsGenerator class. 

![alt text](./examples/img_sequence.png "Image sequence repository")

2. Choose the generated image extension and where you want to save it (otherwise, it will be stored by default in the sequence repository).

3. Generate your star trail image. AND ENJOY :D. 

``` python
from pystartrails import TrailsGenerator

# Initialize the TrailsGenerator class
trails_generator = TrailsGenerator(sequence_repository = "../data/raw/" , generated_img_extension = "JPG", generated_img_name = "trailed_img")

# Generate trails
star_trail_img = trails_generator.generate_trails()

"""
OUTPUT

100%|██████████| 10/10 [00:04<00:00,  2.17it/s]
"""
```

You could also show the generated img using matplotlib. 

``` python
import matplotlib.pyplot as plt 

plt.imshow(star_trail_img)
plt.show()

```
![alt text](./examples/generated_img.jpg "The generated image")



# Dependencies
The PyStarTrails package needs the following packages :

* [matplotlib](https://matplotlib.org/stable/index.html)
* [NumPy](https://numpy.org/)
* [OpenCV](https://opencv.org/)
* [tqdm](https://tqdm.github.io/)


# See Also
All my star trail images were generated using this package. You could check my Instagram account [Yassir LAIRGI](https://www.instagram.com/lairgi_yassir).

# Contribution
Feel free to contact me via the Issues tab on GitHub if you would like to contribute or provide feedback.

# License
Please note that the PyStarTrails package is distributed under the MIT License (MIT).