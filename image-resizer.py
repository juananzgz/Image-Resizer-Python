import argparse
import sys
import cv2
import os

#  Global Variables


parser = argparse.ArgumentParser()
parser.add_argument("--src", metavar="source",
                    help="Source folder of the Image files")
parser.add_argument("--dest", metavar="destinantion",
                    help="Destination folder of the Image files (Default: Source folder)")
parser.add_argument("--size", metavar="size", type=float,
                    help="times you wish to multiply size. Default: 2")
parser.add_argument("--ext", metavar="extension", nargs='+',
                    help="""Extensions of files to be resized (Default: jpg png).
                         Supported extensions - Extensions Supported by OpenCV.""")
args = parser.parse_args()


def resize_image(img, size):
    """Resize the image to given size
    params:
        img - array of image pixels
        size - float
    """
    width = int(img.shape[1] * size)
    height = int(img.shape[0] * size)
    dsize = (width, height)
    dst = cv2.resize(img, dsize, interpolation=cv2.INTER_LINEAR)
    # Applying Gaussian blu
    
    for i in range(1, int(size), 2):
        dst2 = cv2.GaussianBlur(dst, (i, i), 0)

    return dst2


def load_images(src, ext, size):
    """Resize the images in given source folder
    and save to the destinantion folder
    params:
        src - Source folder
        ext - Extensions of images to be 
    """

    cd = os.getcwd()
    os.chdir(src)
    files_ls = os.listdir()
    files = [file for file in files_ls if((len(file.split('.')) > 1) 
             and (file.split('.')[1].lower() in ext))]
    res_imgs = []
    print("Size: x",size)
    for file in files:
        img = cv2.imread(file)
        res_imgs.append((file, resize_image(img, size)))
        print("\nResizing Image:", src + file)

    return res_imgs, cd


def save_images(cd, imgs, src, dest):
    """Save the images to the destination folder
    params:
        cd - Working Directory where program resides
        imgs - list of Tuples => (image name, image)
        src - Source of the image files
        dest - destinantion folder of the image
    """
    os.chdir(cd)
    os.chdir(dest)
    for img in imgs:
        cv2.imwrite(img[0], img[1])
        print("\nSaving Image:", src + img[0],
              "To", dest + img[0])


if args.src == None:
    sys.exit("Path source Folder Missing")


if args.dest == None:
    args.dest = args.src


if args.size == None:
    size = 2
else:
    size = float(args.size)


if args.ext == None:
    args.ext = ['jpg', 'png']


imgs, cd = load_images(args.src, args.ext, size)
save_images(cd, imgs, args.src, args.dest)

