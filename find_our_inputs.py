import glob
import shutil
import sys
import os
if __name__ == '__main__':

    #for filepath in glob.iglob(temp_out + '/**/*', recursive=True):
    for filepath in glob.iglob('inputs/*', recursive=True):

        if filepath.endswith(".in"):
            with open(filepath, 'r') as f0:
                num_student = f0.readline()
                Smax = f0.readline()
                if (float(Smax) == 94.451):
                    print(filepath)
            
