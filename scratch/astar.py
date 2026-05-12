from heapq import heappush, heappop

def aStarTsa(stateSpaceGraph, h, startState, goalState):
    frontier = []
    heappush(frontier, (h[startState], startState))
    print('Initial frontier:',list(frontier))
    explored_order = []
    while frontier:
        node = heappop(frontier)
        if (node[1].endswith(goalState)): return node, explored_order
        print('Exploring:',node[1][-1],'at cost',node[0])
        explored_order.append(node[1][-1])
        for cost, neighbor in stateSpaceGraph.get(node[1][-1], []):
            g = node[0] - h[node[1][-1]]
            new_f = g + cost + h[neighbor]
            heappush(frontier, (new_f, node[1] + neighbor))
        
        print(list(frontier))

ex_graph = {
    'S':[(3,'a'),(2,'d'),(10,'G')],'a':[(5,'b')],
    'd':[(1,'b'),(3,'e')],'G':[],'b':[(1,'e'),(2,'c')],
    'e':[(3,'G')],'c':[(4,'G')]}
h = {'S':7,'a':4,'b':4,'c':2,'d':5,'e':4,'G':0}
print('Solution path:',aStarTsa(ex_graph, h, 'S', 'G'))
