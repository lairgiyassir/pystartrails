# PyStarTrails

![alt text](docs/logo.png "PyStarTrails Logo")

This package can be used by astrophotographers and photographers to create stunning images of the night sky by generating star trails from a sequence of images, and also create beautiful time-lapse videos.

The previous image-processing software I used was Adobe Photoshop, a powerful image-processing program that can be used for the generation of star trails. However, I experienced slow computer performance after uploading a star trail image sequence (more than 500 images) because my RAM became overloaded. I was forced to divide the 500 images into small batches and this process took a considerable amount of time. 

Due to this, I have decided to develop a lightweight and fast python package that does not require the installation of any external programs. I hope that this package will be useful for all astrophotographers and photographers worldwide :) 

Developed by [Yassir LAIRGI](https://lairgiyassir.github.io/) ©2022. 

# Installation
The PyStarTrails package can be installed through pip:

```bash
pip install pystartrails
```

# Usage

## Star Trails Generation

The package assumes that you already have a sequence of night sky images from which you would like to create a star-trail image. In order create your first star-trail image, specify : 

``` python
from pystartrails import TrailsAndTimeLapseGenerator

trails_generator = TrailsAndTimeLapseGenerator(
    sequence_repository=sequence_repository, 
    generated_img_name=generated_img_name,
    generated_img_extension=generated_img_extension, 
    generated_img_repository=generated_img_repository,
    fps=10  # For time-lapse videos
)
star_trail_img = trails_generator.generate_trails()
```

### Parameters:

- **sequence_repository** (str): The image sequence repository (please be sure that your images have the same shape).
- **generated_img_name** (str): The name of your generated image (star trailed image) 
- **generated_img_extension** (str): The extension of your generated image (either "JPG", "JPEG" or "PNG") 
- **generated_img_repository** (str, optional): Here you specify where you want to save your generated trailed image. By default, the generated image is stored in the sequence repository
- **fps** (int, default=10): Frames per second for time-lapse videos
- **output_extension** (str, default='mp4'): The extension of the output time-lapse video

### The `generate_trails()` method:

The `generate_trails()` method returns array in the same format as the input format and saves the generated image in the specified generated_img_repository.

**Parameters:**
- **n_images** (int, optional): Number of images to use from the sequence. If not specified, all images are used. This parameter controls how many images from your sequence will be processed to create the star trails. For example, if you have 100 images and set `n_images=20`, the method will process every 5th image (100/20=5) to create the trails, making the process faster but potentially less detailed.

```python
# Use all images in the sequence
star_trail_img = trails_generator.generate_trails()

# Use only 20 images from the sequence (evenly distributed)
star_trail_img = trails_generator.generate_trails(n_images=20)
```

## Time-lapse Video Creation

The package also supports creating time-lapse videos from your image sequence:

### Regular Time-lapse (without blending):

```python
from pystartrails import TrailsAndTimeLapseGenerator

trails_generator = TrailsAndTimeLapseGenerator(
    sequence_repository="../data/raw/", 
    generated_img_name="timelapse_img",
    generated_img_extension="JPG", 
    fps=30
)

# Create a regular time-lapse video
trails_generator.create_timelapse(
    blended_timelapse=False, 
    output_filename="my_timelapse"
)
```

**Output - Regular Time-lapse:**

[📹 View Regular Time-lapse Video](docs/regular_timelapse.mp4)

### Blended Time-lapse (with star trails accumulation):

```python
# Create a blended time-lapse video where star trails accumulate over time
trails_generator.create_timelapse(
    blended_timelapse=True, 
    output_filename="my_blended_timelapse"
)
```

**Output - Blended Time-lapse:**

[📹 View Blended Time-lapse Video](docs/blended_timelapse.mp4)

**The difference:**
- **blended_timelapse=False**: Creates a regular time-lapse video showing each frame as-is
- **blended_timelapse=True**: Creates a blended time-lapse where star trails accumulate progressively, showing the star trails building up over time

### Video Examples:

**Regular Time-lapse Example:**

[📹 View Regular Time-lapse Video](docs/regular_timelapse.mp4)

**Blended Time-lapse Example (with accumulating star trails):**

[📹 View Blended Time-lapse Video](docs/blended_timelapse.mp4)

# Example

This example demonstrates both star trails generation and time-lapse creation:

1. Prepare the folder of your night sky image sequence. This repository is actually the sequence_repository attribute of TrailsAndTimeLapseGenerator class. 

![alt text](docs/img_sequence.png "Image sequence repository")

2. Choose the generated image extension and where you want to save it (otherwise, it will be stored by default in the sequence repository).

3. Generate your star trail image and create time-lapse videos:

``` python
from pystartrails import TrailsAndTimeLapseGenerator

# Initialize the TrailsAndTimeLapseGenerator class
trails_generator = TrailsAndTimeLapseGenerator(
    sequence_repository="../data/raw/", 
    generated_img_extension="JPG", 
    generated_img_name="trailed_img",
    fps=24
)

# Generate trails using all images
star_trail_img = trails_generator.generate_trails()

# Generate trails using only 50 images (faster processing)
star_trail_img_fast = trails_generator.generate_trails(n_images=50)

# Create a regular time-lapse video
trails_generator.create_timelapse(
    blended_timelapse=False, 
    output_filename="regular_timelapse"
)

# Create a blended time-lapse video with accumulating star trails
trails_generator.create_timelapse(
    blended_timelapse=True, 
    output_filename="blended_timelapse"
)

"""
OUTPUT

100%|██████████| 10/10 [00:04<00:00,  2.17it/s]
100%|██████████| 10/10 [00:02<00:00,  4.50it/s]
100%|██████████| 10/10 [00:15<00:00,  1.50it/s]
Timelapse video saved as regular_timelapse.mp4
100%|██████████| 10/10 [00:18<00:00,  1.35it/s]
Timelapse video saved as blended_timelapse.mp4
"""
```

You can also display the generated image using matplotlib:

``` python
import matplotlib.pyplot as plt 

plt.imshow(star_trail_img)
plt.show()
```

![alt text](docs/generated_img.jpg "The generated star trails image")

### Example Time-lapse Video:

Here's an example of a time-lapse video created using PyStarTrails:

[📹 View Example Time-lapse Video](docs/example_of_timelapse.mp4)

# Dependencies
The PyStarTrails package needs the following packages:

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
