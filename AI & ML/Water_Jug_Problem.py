from collections import deque


def water_jug_problem_trace_path (): 
    jug1_capacity = int (input ("Enter capacity of jug-1: ")) 
    jug2_capacity = int (input ("Enter capacity of jug-2: ")) 
    target = int (input ("Enter target amount: ")) 
    target_jug = int (input ("Enter which jug should reach the target (1 or 2): ")) 
    if target_jug not in [1, 2]: 
        print ("Invalid jug selection. Please enter 1 or 2.") 
        return None 
 
    queue = deque ([((0, 0), [(0, 0)])]) 
    visited = set () 
    visited.add((0, 0)) 
 
    while queue: 
        (current_jug1, current_jug2), path = queue.popleft() 
 
        if (target_jug == 1 and current_jug1 == target) or (target_jug == 2 and current_jug2 == target): 
            return path 
 
        next_states = [] 
 
        next_states.append((jug1_capacity, current_jug2)) 
        next_states.append((current_jug1, jug2_capacity)) 
        next_states.append((0, current_jug2)) 
        next_states.append((current_jug1, 0)) 
        pour = min(current_jug1, jug2_capacity - current_jug2) 
        next_states.append((current_jug1 - pour, current_jug2 + pour)) 
        pour = min(current_jug2, jug1_capacity - current_jug1) 
        next_states.append((current_jug1 + pour, current_jug2 - pour)) 
 
        for state in next_states: 
            if state not in visited: 
                visited.add(state) 
                queue.append((state, path + [state])) 
 
    return None 
 
solution_path = water_jug_problem_trace_path() 
 
if solution_path: 
    print(f"Solution Found! Path: {solution_path}") 
else: 
    print("No solution found.")