import random
import json
import _pickle as pickle


num_students = 50
smax = round(random.uniform(68, 100), 3)
dict = {}

def write_file(num_students):
	for i in range(num_students):
		for j in range(num_students):
			if (i, j) not in dict and i != j and (j,i) not in dict:
				dict[(i,j)] = (round(random.uniform(0, 36), 3), round(random.uniform(1, 26), 3))


	file = 'new' + str(num_students) + '.in'
	with open(file, 'w') as f:
	    print(num_students, file=f)
	    print(smax, file=f)
	    for x in dict:
	    	print(x[0], x[1], dict[x][0], dict[x][1], file=f)

write_file(20)
