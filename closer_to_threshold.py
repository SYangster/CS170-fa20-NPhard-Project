import random

file = 'manual_50.in'
d = dict()
num_students = 0
smax = 0
with open(file) as test:
	text = test.read()
	text = iter(text.splitlines())
	num_students = next(text)
	smax = next(text)
	for line in text:
		tokens = line.split()
		i = int(tokens[0])
		j = int(tokens[1])
		h = float(tokens[2])
		s = float(tokens[3])
		d[(i, j)] = (h, s)

solution_dictionary = {1: [36, 27, 4], 10: [13, 24], 35: [11, 49], 36: [14, 32, 28], 3: [29, 40], 13: [12, 30], 5: [15, 41], 29: [10, 39, 45], 31: [8, 42], 9: [22, 47], 21: [31, 3, 20], 19: [7, 18, 35], 22: [16], 34: [19, 43], 6: [34, 2], 14: [9, 23, 17], 15: [0, 48, 1], 45: [21, 6], 2: [37, 5, 38], 48: [46, 25], 37: [44, 26, 33]}

num_rooms = len(solution_dictionary)

stress_budget = float(smax) / float(num_rooms)

for r in solution_dictionary:
	room = solution_dictionary[r]
	random_size = stress_budget / len(room)
	for i in room:
		for j in room:
			if i != j and (i < j):
				happiness = d[(i, j)][0]
				if (random_size - 0.5) >= 0:
					d[(i, j)] = (happiness, round(random.uniform(random_size-0.5, random_size), 3))
				else:
					d[(i, j)] = (happiness, round(random.uniform(0, random_size), 3))

file = 'manual_50_updated.in'	
with open(file, 'w') as f:
	print(num_students, file=f)
	print(smax, file=f)
	for x in d:
	    print(x[0], x[1], d[x][0], d[x][1], file=f)
