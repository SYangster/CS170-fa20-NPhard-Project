import random
import json
import _pickle as pickle


num_students = 50
smax = round(random.uniform(50, 100), 3)
dict = {}
for i in range(num_students):
	for j in range(num_students):
		if (i, j) not in dict and i != j and (j,i) not in dict:
			dict[(i,j)] = (round(random.uniform(0, 36), 3), round(random.uniform(3, 45), 3))


with open('50.in', 'w') as f:
    print(num_students, file=f)
    print(smax, file=f)
    for x in dict:
    	print(x[0], x[1], dict[x][0], dict[x][1], file=f)