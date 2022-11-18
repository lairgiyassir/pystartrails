from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'Generate a star trail image automatically from a sequence of images'
LONG_DESCRIPTION = 'This package allows astrophotographers and photographers to generate star-trail images quickly and easily.'

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