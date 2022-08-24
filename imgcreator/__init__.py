import os
import json
from PIL import Image
from pylibdmtx.pylibdmtx import encode, decode
import cv2
import numpy

from barcode import UPCA
from barcode.writer import ImageWriter
 
__version__ = '1.0.0'

class ImageManager:
    def __init__(self):
        self.number = 10000000000
        
    def resize_image(self, src, scale_factor):
        width = int(src.shape[1] * scale_factor)
        height = int(src.shape[0] * scale_factor)
        dim = (width, height)
        return cv2.resize(src, dim)

    def binary_image(self, src):
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        return cv2.cvtColor(bw, cv2.COLOR_GRAY2BGR)

    def generate(self, src_folder, dst_folder):
        if not os.path.isdir(src_folder) or not os.path.isdir(dst_folder):
            return
        print('Generating images...')
        
        filelist = os.listdir(src_folder)
        if len(filelist) > 0:
            for file in filelist:
                print(file)
                encoded = encode(file.encode('utf8'))
                img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
                src = numpy.array(img)

                # resize image
                scale_factor = 1.5
                src = self.resize_image(src, scale_factor)
            
                # load image
                dest = cv2.imread(os.path.join(src_folder, file))

                # draw DataMatrix code
                left = 10
                top = 40
                offset = 125
            
                src = self.binary_image(src)
                src[numpy.where((src==[255,255,255]).all(axis=2))] = dest[10, 10]
                dest[top:top + src.shape[0], dest.shape[1] - offset: dest.shape[1] - offset + src.shape[1]] = src
            
                # draw UPCA
                print(self.number)
                number_to_str = str(self.number)
                upca_code = UPCA(str(number_to_str), writer=ImageWriter())
                upca_code.save(number_to_str)

                src = cv2.imread(number_to_str + '.png')
                src = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
            
                # resize upca image
                scale_factor = 0.5
                src = self.resize_image(src, scale_factor)
            
                left = 0
                top = 258
                src = self.binary_image(src)
                src[numpy.where((src==[255,255,255]).all(axis=2))] = dest[10, 10]
                dest[top:top + src.shape[0], left: left + src.shape[1]] = src

                # cv2.imshow(str(i), dest)
                outfile = '{0}x{1}_{2}.png'.format(dest.shape[1], dest.shape[0], file.split('.')[0])
                cv2.imwrite(os.path.join(dst_folder, outfile), dest)
            
                self.number += 1

            # cv2.waitKey(0) 

    