from parse import read_input_file, write_output_file
import networkx as nx

D_10 = {1: 3, 5: 3, 3: 3, 0: 6, 8: 6, 4: 7, 6: 7, 7: 2, 9: 2, 2: 2}

path_10 = 'out/10.out'

write_output_file(D_10, path_10)


D_20 = {17: 10, 18: 10, 11: 9, 16: 9, 1: 1, 7: 1, 9: 4, 13: 11, 5: 11, 14: 7, 6: 7, 2: 2, 19: 2, 4: 3, 3: 3, 12: 8, 15: 8, 8: 13, 0: 13, 10: 15}

path_20 = 'out/20.out'

write_output_file(D_20, path_20)


D_50 = {7: 9, 10: 9, 31: 20, 19: 20, 1: 15, 39: 15, 25: 15, 12: 4, 43: 4, 30: 26, 45: 26, 3: 6, 37: 6, 20: 6, 23: 19, 17: 19, 9: 19, 11: 27, 16: 27, 29: 27, 38: 38, 48: 38, 5: 38, 32: 34, 4: 34, 36: 34, 21: 36, 46: 36, 22: 24, 47: 24, 6: 28, 35: 28, 0: 13, 34: 13, 26: 16, 44: 16, 33: 16, 8: 30, 24: 30, 18: 0, 28: 0, 14: 0, 2: 11, 27: 22, 49: 22, 15: 31, 42: 31, 40: 48, 41: 48, 13: 48}

path_50 = 'out/50.out'

write_output_file(D_50, path_50)