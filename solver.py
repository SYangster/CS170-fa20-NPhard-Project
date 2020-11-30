import networkx as nx
from parse import read_input_file, write_output_file, write_output_file_with_hp
from utils import is_valid_solution, calculate_happiness, convert_dictionary
import sys
import os
import argparse
import glob

import random
import copy

import numpy as np

def solve(G, s, upper_k, max_search_iters):
    """
    Args:
        G: networkx.Graph
        s: stress_budget
    Returns:
        D: Dictionary mapping for student to breakout room r e.g. {0:2, 1:0, 2:1, 3:2}
        k: Number of breakout rooms
    """

    #np.random.seed(99)

    # print(s)
    #print(list(G.adjacency()))

    room_mapping_default = {}
    for student in (G.adjacency()):
        room_mapping_default[student[0]] = [student[0]]
    num_students = len(room_mapping_default)
    #room_mapping = room_mapping_default
    
    upper_k_students = int(num_students * upper_k)
    if upper_k_students <= 2:
        upper_k_students = 2

    #room_mapping = {}    
    room_mapping = generate_start_state(G, s, upper_k_students, max_search_iters)
    if room_mapping is None:
        return (None, None)

    #room_mapping = {21: [2, 42], 22: [13, 34], 11: [7, 0], 4: [45, 25, 8], 2: [38, 48, 5], 25: [31, 11, 16], 5: [28, 18, 19], 23: [40, 47, 41], 18: [21, 46], 12: [22, 49, 1], 8: [4, 32, 14], 6: [12, 30], 15: [10, 39], 9: [44, 24, 27], 3: [3, 37, 20], 38: [9, 23, 17], 35: [43, 26, 29], 1: [15, 33, 36], 45: [6, 35]}       

    #room_mapping = {10: [17, 18], 9: [11, 16], 1: [1, 7], 4: [9], 11: [13, 5], 7: [14, 6], 2: [2, 19], 3: [4, 3], 8: [12, 15], 13: [8, 0], 15: [10]}

    #room_mapping = {3:[1, 5, 3], 6:[0, 8], 7:[4, 6], 2:[7, 9, 2]}

    print("random: " + str(room_mapping))

    best_happiness = 0
    best_D = copy.deepcopy(room_mapping)

    steps = 0
    #next_step = combine_step(G, s, num_students, room_mapping)
    next_step = take_step(G, s, len(room_mapping), room_mapping, False, num_students)
    previous_step = copy.deepcopy(room_mapping)
    while (next_step != 0 and steps <= 50): #HYPERPARAMETER: how many steps in random walk after finding initial state 1000
        steps += 1
        previous_step = copy.deepcopy(next_step)
        next_step = take_step(G, s, len(next_step), next_step, False, num_students)
        #next_step = combine_step(G, s, num_students, room_mapping) 
        print("STEP " + str(steps) + " " + str(next_step))
        
        if (steps % 10 == 0):
            greedy_step = copy.deepcopy(previous_step)
            while (greedy_step != 0):
                previous_greedy = copy.deepcopy(greedy_step)
                print(calculate_happiness(convert_dictionary(previous_greedy), G))
                greedy_step = take_step(G, s, len(greedy_step), greedy_step, True, num_students)
                
                #print(previous_greedy)
                #print(calculate_happiness(convert_dictionary(previous_greedy), G))

            greedy_happiness = calculate_happiness(convert_dictionary(previous_greedy), G) 
            print(is_valid_solution(convert_dictionary(previous_greedy), G, s, len(previous_greedy))) 
            print("HP: " + str(greedy_happiness))
            print(previous_greedy)
            print("")
            if (greedy_happiness > best_happiness):
                best_happiness = greedy_happiness
                best_D = previous_greedy

    room_mapping = best_D
    # for i in G.adjacency():
    #     print(i)
    #     print("")

    # room_mapping = {7:0, 2:0, 1:0, 5:1, 0:1, 9:1, 8:2, 6:2, 3:2, 4:2}
    # return(room_mapping, 3)
    
    print(room_mapping)

    return (convert_dictionary(room_mapping), len(room_mapping))

#ADD A TIMEOUT PARAMETER/BINARY SEARCH THINGY
def generate_start_state(G, s, upper_k, max_search_iters):
    print("finding start state...")
    iter_counter = 0
    while True: 
        iter_counter += 1
        if iter_counter > max_search_iters:
            return None
        print(iter_counter)

        students = []
        for student in (G.adjacency()):
            students.append(student[0])
        k = np.random.randint(1, upper_k) #HYPERPARAMETER: (maybe do binary search) use to pick range of random room numbers
        #k = np.random.randint(1, len(students)/2+3) #HYPERPARAMETER: (maybe do binary search) use to pick range of random room numbers

        invalid_sol = False
        start_state = {}
     
        while students:
            #print(start_state)
            #print(students)
            if invalid_sol:
                break
            remaining_students = copy.deepcopy(students)

            while True:
                orig_start_state = copy.deepcopy(start_state)
                student = remaining_students.pop(np.random.randint(0, len(remaining_students)))
                # room = np.random.randint(0, k)
                # if room in start_state:
                #     start_state[room].append(student)
                # else:
                #     start_state[room] = [student]

                remaining_rooms = [x for x in range(1, k+1)]
                while (len(remaining_rooms) > 0): #HYPERPARAMETER: use to determine what fraction of random rooms to try per student
                    start_state = copy.deepcopy(orig_start_state) 
                    room = remaining_rooms.pop(np.random.randint(0, len(remaining_rooms)))
                    if room in start_state:
                        start_state[room].append(student)
                    else:
                        start_state[room] = [student]

                    if is_valid_solution(convert_dictionary(start_state), G, s, len(start_state)):
                        break

                #maybe rewrite valid solution checker for solutions not with all students
                if is_valid_solution(convert_dictionary(start_state), G, s, len(start_state)):
                    #print(start_state)
                    students.remove(student)
                    break
                elif not remaining_students:
                    invalid_sol = True
                    break
                else:
                    start_state = orig_start_state

        if not invalid_sol:            
            break
        #print(start_state)
    return start_state



def combine_step(G, s, k, room_mapping):
    # print(list(room_mapping.keys()))
    rand_room_from = random.choice(list(room_mapping.keys()))

    rand_room_to = random.choice(list(room_mapping.keys()))
    while (rand_room_to == rand_room_from):
        rand_room_to = random.choice(list(room_mapping.keys()))

    room_mapping_check = copy.deepcopy(room_mapping)

    room_mapping_check[rand_room_to] += (room_mapping_check[rand_room_from])
    room_mapping_check.pop(rand_room_from)
    k -= 1
    stuck = 0
    #print(room_mapping_check.items())
    #print(room_mapping_check)
    while (not is_valid_solution(convert_dictionary(room_mapping_check), G, s, k)):
        stuck += 1
        if (stuck > 1200):
            return 0
        k += 1

        rand_room_from = random.choice(list(room_mapping.keys()))
        rand_room_to = random.choice(list(room_mapping.keys()))
        while (rand_room_to == rand_room_from):
            rand_room_to = random.choice(list(room_mapping.keys()))

        room_mapping_check = copy.deepcopy(room_mapping)

        room_mapping_check[rand_room_to] += (room_mapping_check[rand_room_from])
        room_mapping_check.pop(rand_room_from)
        k -= 1
    
    return room_mapping_check



def take_step(G, s, k, room_mapping, greedy_bool, num_students):
    current_happiness = calculate_happiness(convert_dictionary(room_mapping), G)
    stuck = 0
    epsilon_upper = 1.0
    epsilon_cutoff = 1.0 #I NEED TO FIX THIS, but maybe simulated annealing isn't it
    #print(epsilon_param)
    
    next_mapping = copy.deepcopy(room_mapping)

    rooms_from = [room for room in room_mapping.keys()]
    while(rooms_from):
        rand_room_from = rooms_from.pop(np.random.randint(0, len(rooms_from)))
        students = copy.deepcopy(room_mapping[rand_room_from])
        

        while (students):
            
            rand_student = students.pop(np.random.randint(0, len(students)))
            rooms_to = [room for room in range(0, num_students)]
            rooms_to.remove(rand_room_from)

            while (rooms_to):
                            
                if epsilon_upper > epsilon_cutoff: #hyperparameter: use for temperature/epsilon for chance to go downhill at a step
                    epsilon_upper -= 0.006
                epsilon_param = np.random.uniform(0,epsilon_upper)

                next_mapping = copy.deepcopy(room_mapping)
                rand_room_to = rooms_to.pop(np.random.randint(0, len(rooms_to)))
                if rand_room_to in room_mapping:
                    next_mapping[rand_room_to].append(rand_student)
                else:
                    next_mapping[rand_room_to] = [rand_student]


                next_mapping[rand_room_from].remove(rand_student)
                if not next_mapping[rand_room_from]:
                    next_mapping.pop(rand_room_from)

                if (not is_valid_solution(convert_dictionary(next_mapping), G, s, len(next_mapping))
                or (calculate_happiness(convert_dictionary(next_mapping), G) <= current_happiness and (epsilon_param < epsilon_cutoff) and greedy_bool)):
                    continue 
                else:
                    return next_mapping
                break
    return 0

    

# Here's an example of how to run your solver.
# Usage: python3 solver.py test.in

if __name__ == '__main__':
    assert len(sys.argv) == 5
    input_path = sys.argv[1] #inputs/small
    output_path = sys.argv[2] #temp_out/small
    iterations = int(sys.argv[3]) #at least enough to do the binary search
    max_search_iters = int(sys.argv[4]) #500 to 2000


    inputs = glob.glob(str(input_path) + '/*') #inputs/small
    for path in inputs:
    
        head, tail = os.path.split(path)

        G, s = read_input_file(path)
        # D, k = solve(G, s)
        # assert is_valid_solution(D, G, s, k)
        # print("Total Happiness: {}".format(calculate_happiness(D, G)))
        
        max_happiness = 0
        max_D = {}
        max_k = 0
        for student in (G.adjacency()):
            max_k += 1 

        upper_k = 0.5
        k_ceiling = 1.0
        k_floor = 0.0

        for i in range(0, iterations): #HYPERPARAMETER: how many iterations of whole algorithm to do
            print("Iteration:" + str(i) + " UpperK: " + str(upper_k))
            D, k = solve(G, s, upper_k, max_search_iters) #BINARY SEARCH THISSS, 500 to 2000 seems like a good number
            if D is None:
                k_floor = upper_k
                upper_k = upper_k + (k_ceiling-upper_k)/2
                continue
            else:
                k_ceiling = upper_k
                upper_k = k_floor + (upper_k-k_floor)/2

            assert is_valid_solution(D, G, s, k)
            happiness = calculate_happiness(D, G)
            print("HP: " + str(happiness))
            print("")
            if (happiness > max_happiness):
                max_happiness = happiness
                max_D = D
                max_k = k
            print("maxHP: " + str(max_happiness))
            print("max_D: " + str(max_D))
            print("")

        assert is_valid_solution(max_D, G, s, max_k)
        print("BEST SOL: " + str(max_D))
        print("Total Happiness: {}".format(calculate_happiness(max_D, G)))

        #TODO, script to compare two folders? useful for combining results later
        #TODO, script to run command with diff parameters for each 10,20,50 type, over a folder for certain number of iterations
        #TODO, hone in process
        #TODO, if out file already exists, first compare before overwriting
        #write_output_file_with_hp(max_D, max_happiness, str(output_path) + '/' + basename(normpath(input_path))[:-3]  + '.out') #FIX OUTPUTS TO GO TO FOLDERS ETC.. different names

        if (os.path.exists(str(output_path) + '/' + str(tail)[:len(tail)-3]  + '.out')):
            with open(str(output_path) + '/' + str(tail)[:len(tail)-3]  + '.out', "r") as fo:
                nodes = set()
                rooms = set()
                D = {}
                lines = fo.read().splitlines()
                fo.close()
                existing_happiness = lines[0]

            if max_happiness > float(existing_happiness):
                write_output_file_with_hp(max_D, max_happiness, str(output_path) + '/' + str(tail)[:len(tail)-3]  + '.out') #FIX OUTPUTS TO GO TO FOLDERS ETC.. different names
        else:
            write_output_file_with_hp(max_D, max_happiness, str(output_path) + '/' + str(tail)[:len(tail)-3]  + '.out') #FIX OUTPUTS TO GO TO FOLDERS ETC.. different names

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
