import json
from setuptools.command import build_ext
from setuptools import setup, Extension
import sys
import os
import io
from setuptools.command.install import install
import platform
import shutil
from pathlib import Path
import site


long_description = io.open("README.md", encoding="utf-8").read()

def copyfiles(src, dst):
    if os.path.isdir(src):
        filelist = os.listdir(src)
        for file in filelist:
            libpath = os.path.join(src, file)
            shutil.copy2(libpath, dst)
    else:
        shutil.copy2(src, dst)

class CustomBuildExt(build_ext.build_ext):
    def run(self):
        build_ext.build_ext.run(self)

class CustomBuildExtDev(build_ext.build_ext):
    def run(self):
        build_ext.build_ext.run(self)
    
class CustomInstall(install):
    def run(self):
        install.run(self)


setup(name='barcode-image-composer',
      version='1.0.0',
      description='Compose images with barcode, QR code, and DataMatrix code.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='yushulx',
      url='https://github.com/yushulx/barcode-image-composer',
      license='MIT',
      packages=['imgcomposer'],
      classifiers=[
           "Development Status :: 5 - Production/Stable",
           "Environment :: Console",
           "Intended Audience :: Developers",
          "Intended Audience :: Education",
          "Intended Audience :: Information Technology",
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: MIT License",
          "Operating System :: Microsoft :: Windows",
          "Operating System :: MacOS",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3 :: Only",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10",
          "Topic :: Scientific/Engineering",
          "Topic :: Software Development",
      ],
      install_requires=['python-barcode', 'pylibdmtx', 'pillow', 'qrcode'],
      entry_points={
          'console_scripts': ['imgcompose=composer.scripts:imgcompose']
      },
      cmdclass={
          'install': CustomInstall,
          'build_ext': CustomBuildExt,
          'develop': CustomBuildExtDev},
      )
