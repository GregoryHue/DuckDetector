# Quick script to resize images that are too large. Also slighty degrades the quality in order to save on storage and memory.

from PIL import Image
import os, sys

MIN_SIZE = 1024
PATH = "dataset/test/non-Duck/"

dirs = os.listdir( PATH )

i = 0
j  = len(dirs)

for item in dirs:
    if os.path.isfile(PATH+item):
        im = Image.open(PATH+item)
        f, e = os.path.splitext(PATH+item)
        
        if im.width > MIN_SIZE:
            new_height = round(im.height / (im.width / MIN_SIZE))
            print('width: ', im.width, '| height: ', im.height, '| new width: ', MIN_SIZE, '| new height: ', new_height)
            imResize = im.resize((MIN_SIZE, new_height), Image.ANTIALIAS)
            imResize.save(f + '.jpg', 'JPEG', quality=90)
        elif im.height > MIN_SIZE:
            new_width = round(im.width / (im.height / MIN_SIZE))
            print('width: ', im.width, '| height: ', im.height, '| new width: ', new_width, '| new height: ', MIN_SIZE)
            imResize = im.resize((new_width, MIN_SIZE), Image.ANTIALIAS)
            imResize.save(f + '.jpg', 'JPEG', quality=90)
        else:
            imResize = im.resize((im.width, im.height), Image.ANTIALIAS)
            print('width: ', im.width, '| height: ', im.height, '| new width: ', '*', '| new height: ', '*')
            imResize.save(f + '.jpg', 'JPEG', quality=90)
        i = i +1
        print(str(i) + ' images out of ' + str(j) + ' | ', end='')

    
