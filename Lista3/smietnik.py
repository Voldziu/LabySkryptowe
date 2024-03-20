import sys
from os import environ
import os


if __name__=="__main__":
    path = os.getenv('PATH')
    print(path)
    if path:
        directories = path.split(os.pathsep)
        for directory in directories:
            print(os.listdir(directory))



