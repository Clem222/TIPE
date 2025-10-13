import numpy as np

#Graph class (numpy matrice)
class Graph:
    def __init__(self, graph_list, node_list, height, width):
        self.graph=np.array(graph_list).reshape(height, width)
        for x in range(height):
            self.graph[x,x]=0
        self.graph_pheromone = np.ones_like(self.graph, dtype=np.dtype(np.float64))
        self.node_list=node_list
