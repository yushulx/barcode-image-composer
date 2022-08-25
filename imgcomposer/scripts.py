import argparse
import imgcomposer
import sys
import numpy as np
import os

def imgcompose():
    parser = argparse.ArgumentParser(description='Generate barcode QR code image set')
    parser.add_argument('-s', '--src', type=str, help='Image source folder')
    parser.add_argument('-d', '--dst', type=str, help='Image output folder')
    args = parser.parse_args()
    try:
        src_folder = args.src
        dst_folder = args.dst
        
        if not os.path.isdir(src_folder):
            print('Invalid source folder')
            return
        
        if not os.path.isdir(dst_folder):
            os.mkdir(dst_folder)
            
        imgcomposer.ImageManager().generate(src_folder, dst_folder)
    
    except Exception as err:
        print(err)
        sys.exit(1)
