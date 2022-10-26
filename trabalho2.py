import math
import copy

def print_state(state_list):
    for l in state_list:
        print('{0} - {1} - {2}'.format(l[0], l[1], l[2]))

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def find_zero(state_list):
    for i in range(len(state_list)):
        for j in range(len(state_list[i])):
            if state_list[i][j] == 0:
                return (i, j)
# TAREFA 1
def find_all_states(graph, states, goal_state):
    j = 0
    state_lists = copy.deepcopy(states)
    state_list = state_lists[j]
    x1, y1 = find_zero(state_list)
    save_x1 = x1
    save_y1 = y1
    while state_list != goal_state:
        l = []
        for x2 in range(len(state_list)):
            for y2 in range(len(state_list)):
                if manhattan_distance(x1, y1, x2, y2) == 1:
                    if save_x1 != x2 or save_y1 != y2:
                        new_state = copy.deepcopy(state_list)
                        aux = new_state[x2][y2]
                        new_state[x2][y2] = 0
                        new_state[x1][y1] = aux
                        states.append(new_state)
                        i = len(states) - 1
                        l.append(i)
                        graph[i] = [j]
        for el in l:
            graph[j].append(el)
        j += 1
        k = graph[j][0]
        save_x1, save_y1 = find_zero(states[k])
        state_lists = copy.deepcopy(states)
        state_list = copy.deepcopy(state_lists[j])
        x1, y1 = find_zero(state_list)
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
states = [initial_state]
graph = {0:[]}

# Testes goal_state
#goal_state = [[1,2,3],[4,5,6],[7,8,0]]
goal_state = [[1,2,3],[4,0,6],[7,5,8]]

# CHAMADA TAREFA 1
graph_res, states_res = find_all_states(graph, states, goal_state)
print(graph_res)
print()
for m in range(0, len(states_res)):
    print("{0} -  {1}".format(m, states_res[m]))
    print()

# CHAMADA TAREFA 2
visited = BFS(graph_res, 1)
if len(visited) == len(states_res):
    print("Número de componentes conexos: ", len(visited))