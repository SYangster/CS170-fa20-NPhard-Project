import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_happiness, convert_dictionary
import sys

import random
import copy

#from k_means_constrained import KMeansConstrained
import numpy as np

def solve(G, s):
    """
    Args:
        G: networkx.Graph
        s: stress_budget
    Returns:
        D: Dictionary mapping for student to breakout room r e.g. {0:2, 1:0, 2:1, 3:2}
        k: Number of breakout rooms
    """

    # TODO: your code here!
    # print(s)

    room_mapping = {}
    for student in (G.adjacency()):
        room_mapping[student[0]] = [student[0]]
    num_rooms = len(room_mapping)
    num_students = num_rooms
    
    current_best_happiness = 0
    current_best_D = copy.deepcopy(room_mapping)

    outer_counter = 0
    #next_step = take_step2(G, s, num_rooms, room_mapping, False, num_students)
    next_step = take_step(G, s, num_rooms, room_mapping)
    previous_step = copy.deepcopy(room_mapping)
    random_search = False
    while (previous_step != 0 and outer_counter <= 300):
        outer_counter += 1
        #next_step = take_step2(G, s, len(next_step), next_step, False, num_students)
        if next_step == 0 or random_search:
            random_search = True
            next_step = previous_step
            next_step = take_step2(G, s, len(next_step), next_step, False, num_students)
            previous_step = copy.deepcopy(next_step)
        else:
            previous_step = copy.deepcopy(next_step)
            next_step = take_step(G, s, num_rooms, next_step)

       
        print(next_step)

        greedy_step = copy.deepcopy(previous_step)
        while (greedy_step != 0):
            previous_greedy = copy.deepcopy(greedy_step)
            greedy_step = take_step2(G, s, len(greedy_step), greedy_step, True, num_students)
            
            #print(previous_greedy)
            #print(calculate_happiness(convert_dictionary(previous_greedy), G))

        greedy_happiness = calculate_happiness(convert_dictionary(previous_greedy), G) 
        print("HP: " + str(greedy_happiness))
        print(previous_greedy)
        print("")
        if (greedy_happiness > current_best_happiness):
            current_best_happiness = greedy_happiness
            current_best_D = previous_greedy



        #print("")

    room_mapping = current_best_D

    # for i in G.adjacency():
    #     print(i)
    #     print("")

    # room_mapping = {7:0, 2:0, 1:0, 5:1, 0:1, 9:1, 8:2, 6:2, 3:2, 4:2}
    # return(room_mapping, 3)
    
    print(room_mapping)

    return (convert_dictionary(room_mapping), len(room_mapping))
    pass


def take_step(G, s, num_rooms, room_mapping):
    # print(list(room_mapping.keys()))
    rand_room_from = random.choice(list(room_mapping.keys()))

    rand_room_to = random.choice(list(room_mapping.keys()))
    while (rand_room_to == rand_room_from):
        rand_room_to = random.choice(list(room_mapping.keys()))

    room_mapping_check = copy.deepcopy(room_mapping)

    room_mapping_check[rand_room_to] += (room_mapping_check[rand_room_from])
    room_mapping_check.pop(rand_room_from)
    num_rooms -= 1
    stuck = 0
    #print(room_mapping_check.items())
    #print(room_mapping_check)
    while (not is_valid_solution(convert_dictionary(room_mapping_check), G, s, num_rooms)):
        stuck += 1
        if (stuck > 500):
            return 0
        num_rooms += 1

        rand_room_from = random.choice(list(room_mapping.keys()))
        rand_room_to = random.choice(list(room_mapping.keys()))
        while (rand_room_to == rand_room_from):
            rand_room_to = random.choice(list(room_mapping.keys()))

        room_mapping_check = copy.deepcopy(room_mapping)

        room_mapping_check[rand_room_to] += (room_mapping_check[rand_room_from])
        room_mapping_check.pop(rand_room_from)
        num_rooms -= 1
    
    return room_mapping_check



def take_step2(G, s, num_rooms, room_mapping, greedy_bool, num_students):
    current_happiness = calculate_happiness(convert_dictionary(room_mapping), G)
    
    rand_room_from = random.choice(list(room_mapping.keys()))
    rand_student = random.choice(room_mapping[rand_room_from])
    rand_room_to = np.random.randint(0, num_students)
    while (rand_room_to == rand_room_from):
        rand_room_to = random.choice(list(room_mapping.keys()))

    room_mapping_check = copy.deepcopy(room_mapping)

    if not rand_room_to in room_mapping_check:
        room_mapping_check[rand_room_to] = [rand_student]
        num_rooms += 1
    else:
        room_mapping_check[rand_room_to].append(rand_student)
    room_mapping_check[rand_room_from].remove(rand_student)
    undo_num_rooms = False
    if not room_mapping_check[rand_room_from]:
        room_mapping_check.pop(rand_room_from)
        num_rooms -= 1

        if (not is_valid_solution(convert_dictionary(room_mapping_check), G, s, num_rooms)):
            undo_num_rooms = True
    
    stuck = 0
    
    epsilon_upper = 1.0
    epsilon_param = np.random.uniform(0,1)
    #print(epsilon_param)
    while (not is_valid_solution(convert_dictionary(room_mapping_check), G, s, num_rooms) 
    or (calculate_happiness(convert_dictionary(room_mapping_check), G) <= current_happiness and (epsilon_param < 0.8) and greedy_bool)):
        if epsilon_upper > 0.8:
            epsilon_upper -= 0.003
        epsilon_param = np.random.uniform(0,epsilon_upper)
        #print("2 " + str(epsilon_param))
        if (undo_num_rooms):
            num_rooms += 1
            undo_num_rooms = False
        stuck += 1  
        if (stuck > 500):
            return 0
       
        rand_room_from = random.choice(list(room_mapping.keys()))
        rand_student = random.choice(room_mapping[rand_room_from])
        rand_room_to = np.random.randint(0, num_students)
        while (rand_room_to == rand_room_from):
            rand_room_to = random.choice(list(room_mapping.keys()))

        room_mapping_check = copy.deepcopy(room_mapping)
        if not rand_room_to in room_mapping_check:
            room_mapping_check[rand_room_to] = [rand_student]
            num_rooms += 1
        else:
            room_mapping_check[rand_room_to].append(rand_student)

        room_mapping_check[rand_room_from].remove(rand_student)
        if not room_mapping_check[rand_room_from]:
            room_mapping_check.pop(rand_room_from)
            num_rooms -= 1

            if (not is_valid_solution(convert_dictionary(room_mapping_check), G, s, num_rooms)):
                undo_num_rooms = True

    return room_mapping_check






# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

if __name__ == '__main__':
    assert len(sys.argv) == 2
    path = sys.argv[1]
    G, s = read_input_file(path)
    # D, k = solve(G, s)
    # assert is_valid_solution(D, G, s, k)
    # print("Total Happiness: {}".format(calculate_happiness(D, G)))
    
    max_happiness = 0
    max_D = {}
    max_k = 0
    for i in range(0, 200):
        print("Iteration:" + str(i))
        D, k = solve(G, s)
        assert is_valid_solution(D, G, s, k)
        happiness = calculate_happiness(D, G)
        print("HP: " + str(happiness))
        print("")
        if (happiness > max_happiness):
            max_happiness = happiness
            max_D = D
            max_k = k

    assert is_valid_solution(max_D, G, s, max_k)
    print("BEST SOL: " + str(max_D))
    print("Total Happiness: {}".format(calculate_happiness(max_D, G)))


    write_output_file(D, 'out/test.out')


# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
# if __name__ == '__main__':
#     inputs = glob.glob('file_path/inputs/*')
#     for input_path in inputs:
#         output_path = 'file_path/outputs/' + basename(normpath(input_path))[:-3] + '.out'
#         G, s = read_input_file(input_path, 100)
#         D, k = solve(G, s)
#         assert is_valid_solution(D, G, s, k)
#         cost_t = calculate_happiness(T)
#         write_output_file(D, output_path)