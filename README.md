# Image Resizer Using Pyhton
I modified the original project from <a href="https://github.com/piyush2896/Image-Resizer-Python/commits?author=piyush2896">piyush2896</a> to allow to multiply the original size in order to keep image proportions if there are photos with different sizes in the folder. I added a blur filter to improve results when you increase size. 

## Usage

```
image-resizer.py [-h] [--src source] [--dest destinantion]
                        [--size size [size ...]]
                        [--ext extension [extension ...]]

optional arguments:
  -h, --help            show this help message and exit
  --src source          Source folder of the Image files
  --dest destinantion   Destination folder of the Image files (Default: Source
                        folder)
  --size size [size ...]
                        Times you wish to multiply size (Floats allowed). Default: 2
  --ext extension [extension ...]
                        Extensions of files to be resized (Default: jpg png).
						Supported extensions - Extensions Supported by OpenCV.
```

## Dependencies
Only dependecy is **OpenCV2**
