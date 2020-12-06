import os 
import shutil

f = open("failed.txt", "r")
line = f.readline()
next_line = f.readline()
directory = "failed_inputs"
os.mkdir(directory) 
while line != "" and next_line != "":
	next_line = int(next_line)
	if (next_line > 1):
		file_name = "inputs/" + line.rstrip() + '.in'
		shutil.copy(file_name, directory)
	line = f.readline()
	next_line = f.readline()
	
