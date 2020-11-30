import glob
import shutil
import sys
import os

if __name__ == '__main__':
    for filepath in glob.iglob('best_out/**/*', recursive=True):

        if filepath.endswith(".out"):

            directories = filepath.split('/') # ['test_out', 'medium', 'medium-01.out']
            size_folder = directories[1]      #       0          1           2
            filename = directories[2]

            with open(filepath, "r") as f:
                lines = f.readlines()
            with open("outputs/" + filename, "w") as f:
                firstLine = True
                for line in lines:
                    if not firstLine:
                        f.write(line)
                    firstLine = False

