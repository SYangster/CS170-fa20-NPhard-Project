import networkx as nx
from utils import is_valid_solution, calculate_happiness, convert_dictionary
from parse import read_input_file, write_output_file

D = {36: 24, 27: 24, 4: 24, 2: 15, 0: 15, 40: 3, 47: 3, 41: 3, 9: 18, 23: 18, 17: 18, 3: 9, 37: 9, 20: 9, 1: 21, 32: 21, 44: 5, 33: 5, 26: 5, 30: 4, 12: 22, 43: 22, 25: 26, 42: 26, 21: 17, 6: 17, 46: 16, 35: 16, 31: 14, 19: 14, 49: 8, 15: 8, 22: 11, 7: 11, 24: 13, 8: 13, 48: 23, 38: 23, 5: 23, 16: 25, 11: 25, 29: 25, 39: 6, 10: 6, 45: 6, 34: 10, 13: 10, 28: 38, 18: 38, 14: 38}

path = 'manual_inputs/manual_50_updated.in'

G, s = read_input_file(path)

rooms = 21

print(is_valid_solution(D, G, s, rooms))
