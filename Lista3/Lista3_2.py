import os,sys


if __name__=="__main__":
    path = os.getenv('PATH')
    print(path)
    if path:
        directories = path.split(os.pathsep)
        for directory in directories:
            try:
                print(os.listdir(directory))
            except FileNotFoundError:
                print(f'Problem with directory {directory}, exception caught',file=sys.stderr)