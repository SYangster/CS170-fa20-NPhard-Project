import random
import numpy as np

file = 'final_inputs/20.in'
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

ratios = {}
for pair in d:
	ratios[pair] = d[pair][0]/d[pair][1]

sorted_pairs = (sorted(ratios, key=ratios.get))
# print(sorted_pairs)
# sorted_ratios = {}
# for pair in sorted_pairs:
# 	sorted_ratios[pair] = ratios[pair]
# print(sorted_ratios)
# print(d)
# pair = sorted_pairs[0]
# pair_above = sorted_pairs[1]
# ratio = ratios[pair]
# ratio_above = ratios[pair_above]
# while (ratio <= ratio_above and ratio >= 0 and d[pair][1] >= 0):
# 	ratios[pair] = ratio
# 	d[pair] = (d[pair][0], round(d[pair][1]-0.002, 3))
# 	ratio = d[pair][0]/d[pair][1]

# ratios[pair] = ratio

for i in range(1, len(sorted_pairs)-1):
	pair = sorted_pairs[i]
	pair_above = sorted_pairs[i+1]
	pair_below = sorted_pairs[i-1]
	ratio = ratios[pair]
	ratio_below = ratios[pair_below]
	ratio_above = ratios[pair_above]
	while (ratio > ratio_below and ratio < ratio_above and d[pair][1] >= 0):
		ratios[pair] = ratio
		d[pair] = (d[pair][0], round(d[pair][1]-0.002, 3))
		ratio = d[pair][0]/d[pair][1]

# pair = sorted_pairs[len(sorted_pairs)-1]
# pair_below = sorted_pairs[len(sorted_pairs)-2]
# ratio = ratios[pair]
# ratio_below = ratios[pair_below]
# while (ratio >= ratio_below and ratio >= 0 and d[pair][1] > 0):
# 	if (d[pair][1]-0.002) > 0:
# 		d[pair] = (d[pair][0], round(d[pair][1]-0.002, 3))
# 		ratio = d[pair][0]/d[pair][1]
# ratios[pair]=ratio
# sorted_ratios[pair] = ratio

# sorted_pairs_after = (sorted(ratios, key=ratios.get))
# print(sorted_pairs_after)
# for i in range(len(sorted_pairs)):
# 	if sorted_pairs[i]!=sorted_pairs_after[i]:
# 		print('here')
# for pair in sorted_pairs:
# 	sorted_ratios[pair] = ratios[pair]
# print(sorted_ratios)
# print(d)

file = 'manual_20_ratios.in'	
with open(file, 'w') as f:
	print(num_students, file=f)
	print(smax, file=f)
	for x in d:
	    print(x[0], x[1], d[x][0], d[x][1], file=f)