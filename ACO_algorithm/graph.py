import numpy as np

#Graph class (numpy matrix)
class Graph:
    def __init__(self, graph_list, node_list, height, width):
        self.graph=np.array(graph_list).reshape(height, width)  #main graph used to represent every nodes
        for y in range(height):
            for x in range(width):
                if self.graph[y][x] == -1:
                    self.graph[y][x] = self.graph[x][y]  #makes the matrix symmetric
        for x in range(height):
            self.graph[x,x]=0 #avoid nodes to loopback on themselves
        self.graph_pheromone = np.ones_like(self.graph, dtype=np.dtype(np.float64))
        self.node_list=node_list

    def remove_subpath(self, node_in, node_out):
        self.graph[node_in][node_out]=100000
        self.graph[node_out][node_in]=100000
