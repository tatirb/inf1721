import math
import copy

def print_state(state):
    for l in state:
        print('{0} - {1} - {2}'.format(l[0], l[1], l[2]))

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def find_zero(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return (i, j)
# TAREFA 1
def find_all_states(graph, initial_state):
    j = 0
    states = [initial_state]
    current_parent = states[j]
    x1, y1 = find_zero(current_parent)
    save_x1 = x1
    save_y1 = y1
    while len(current_parent) > 0:
        l = []
        print(len(states))
        for x2 in range(len(current_parent)):
            for y2 in range(len(current_parent)):
                if manhattan_distance(x1, y1, x2, y2) == 1:
                    if save_x1 != x2 or save_y1 != y2:
                        new_state = copy.deepcopy(current_parent)
                        aux = new_state[x2][y2]
                        new_state[x2][y2] = 0
                        new_state[x1][y1] = aux
                        for key,value in enumerate(states):
                            if new_state == value:
                                l.append(key)
                                graph[key].append(j)
                                break
                        states.append(new_state)
                        i = len(states) - 1
                        l.append(i)
                        graph[i] = [j]
        for el in l:
            graph[j].append(el)
        j += 1
        k = graph[j][0]
        save_x1, save_y1 = find_zero(states[k])
        current_parent = copy.deepcopy(states[j])
        x1, y1 = find_zero(current_parent)
    return graph, states

# TAREFA 2
def BFS(G, s):
    visited = []
    L = []
    visited.append(s)    
    L.append(s)
    i = 0
    while L:
        m = L.pop(0)
        for v in G[m]:
            if v not in visited:
                L.append(v)
                visited.append(v)
    return visited

initial_state = [[1,2,3],[0,4,6],[7,5,8]]
graph = {0:[]}

# CHAMADA TAREFA 1
graph_res, states_res = find_all_states(graph, initial_state)

for m in range(0, len(states_res)):
    print("{0} -  {1}".format(m, states_res[m]))
    print()

# CHAMADA TAREFA 2
visited = BFS(graph_res, 1)
if len(visited) == len(states_res):
    print("Número de componentes conexos: ", 1)

# CHAMADA TAREFA 3
graph_3 = [[1,2,3],[4,5,6],[7,8,0]]