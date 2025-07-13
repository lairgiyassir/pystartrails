from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.4'
DESCRIPTION = 'Generate stunning star trail images and time-lapse videos from night sky image sequences'
LONG_DESCRIPTION = 'PyStarTrails is a lightweight Python package designed for astrophotographers and photographers to create beautiful star trail images and time-lapse videos from sequences of night sky images. Features include fast processing, color temperature adjustment, noise reduction, and support for both regular and blended time-lapse videos. A powerful alternative to Adobe Photoshop for star trail generation without the memory overhead.'

# Setting up
setup(
    name="pystartrails",
    version=VERSION,
    author="Yassir LAIRGI",
    author_email="<yassirlairgi@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['matplotlib', 
    'numpy',
    'opencv_python',
    'setuptools',
    'tqdm'
    ],
    keywords=['python', 'star trails', 'astrophotography', 'photography', 'blending modes'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)