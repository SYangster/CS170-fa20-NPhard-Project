dict = {1: 10, 9: 10, 4: 18, 7: 18, 18: 5, 13: 5, 11: 0, 3: 0, 14: 15, 19: 15, 12: 7, 8: 7, 10: 17, 0: 17, 15: 4, 16: 4, 5: 9, 2: 9, 6: 1, 17: 1}

room_dict = {}

for person in dict:
	if (dict[person] in room_dict):
		room_dict[dict[person]].append(person)
	else:
		room_dict[dict[person]] = [person]

print(room_dict)
