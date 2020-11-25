import networkx as nx
from utils import is_valid_solution, calculate_happiness, convert_dictionary
from parse import read_input_file, write_output_file

D = {1: 10, 9: 10, 4: 18, 7: 18, 18: 5, 13: 5, 11: 0, 3: 0, 14: 15, 19: 15, 12: 7, 8: 7, 10: 17, 0: 17, 15: 4, 16: 4, 5: 9, 2: 9, 6: 1, 17: 1}


path = 'new_manual_20.in'

G, s = read_input_file(path)

rooms = 21

print(is_valid_solution(D, G, s, rooms))


# BEST SOL: {1: 10, 9: 10, 4: 18, 7: 18, 18: 5, 13: 5, 11: 0, 3: 0, 14: 15, 19: 15, 12: 7, 8: 7, 10: 17, 0: 17, 15: 4, 16: 4, 5: 9, 2: 9, 6: 1, 17: 1}
# Total Happiness: 233.04600000000005