from parse import read_input_file, write_output_file
from utils import convert_dictionary
import networkx as nx

D_10 = {1: 3, 5: 3, 3: 3, 0: 6, 8: 6, 4: 7, 6: 7, 7: 2, 9: 2, 2: 2}

path_10 = 'out/10.out'

write_output_file(D_10, path_10)


D_20 = {17: 10, 18: 10, 11: 9, 16: 9, 1: 1, 7: 1, 9: 4, 13: 11, 5: 11, 14: 7, 6: 7, 2: 2, 19: 2, 4: 3, 3: 3, 12: 8, 15: 8, 8: 13, 0: 13, 10: 15}

path_20 = 'out/20.out'

write_output_file(D_20, path_20)


D_50 = {21: [2, 42], 22: [13, 34], 11: [7, 0], 4: [45, 25, 8], 2: [38, 48, 5], 25: [31, 11, 16], 5: [28, 18, 19], 23: [40, 47, 41], 18: [21, 46], 12: [22, 49, 1], 8: [4, 32, 14], 6: [12, 30], 15: [10, 39], 9: [44, 24, 27], 3: [3, 37, 20], 38: [9, 23, 17], 35: [43, 26, 29], 1: [15, 33, 36], 45: [6, 35]}
D_50 = convert_dictionary(D_50)

path_50 = 'out/50.out'

write_output_file(D_50, path_50)