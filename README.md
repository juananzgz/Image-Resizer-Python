# Image Resizer Using Pyhton
I modified the original <a href="https://github.com/piyush2896/Image-Resizer-Python/commits?author=piyush2896">piyush2896</a> project to allow to multiply the original size in order to keep image proportions if there are photos with different sizes in the folder. I added a blur filter to improve results when you increase size. 
The only thing that changes from the original project usage is that in --size you have to introduce a float (instead of two integers) 

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
                        Times you wish to multiply size (Floats allowed). If number is from 0 to 1, the image will be reduced. Default: 2
  --ext extension [extension ...]
                        Extensions of files to be resized (Default: jpg png).
						Supported extensions - Extensions Supported by OpenCV.
```

## Dependencies
Only dependecy is **OpenCV2**
