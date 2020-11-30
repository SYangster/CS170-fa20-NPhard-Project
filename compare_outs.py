import glob
import shutil
import sys
import os

# Inputs: best_out, temp_out folders
# -> small, medium, large folders inside
# -> small-#.out

def compare(bestFile, tempFile):  # path strings
    with open(bestFile, 'r') as f1:
        value1 = f1.readline()
    with open(tempFile, 'r') as f2:
        value2 = f2.readline()
    if float(value1) > float(value2):
        best_path = bestFile
    else:
        best_path = tempFile
    return best_path

if __name__ == '__main__':
    assert len(sys.argv) == 2
    #best_out = sys.argv[1]
    temp_out = sys.argv[1]

    #for filepath in glob.iglob(temp_out + '/**/*', recursive=True):
    for filepath in glob.iglob(temp_out + '/*', recursive=True):

        if filepath.endswith(".out"):
            directories = filepath.split('/') # ['test_out', 'medium', 'medium-01.out']
            size_folder = directories[1][:-1]  #       0          1           2
            filename = directories[2]

            best_file_path = 'best_out/' + size_folder + '/' + filename #for size_folder, maybe do size folder minus the last char, for medium0 -> medium
            
            if (os.path.exists(best_file_path)):
                filepath_with_best = compare(best_file_path, filepath)

                if best_file_path != filepath_with_best:
                    shutil.move(filepath_with_best, best_file_path)
            else:
                shutil.move(filepath, best_file_path)

    print("Updated /best_out")
