import numpy as np
from ant import Ant
from graph import Graph

class Swarm:
    def __init__(self, graph, ant_amount, starter_node, path_iteration, delta):
        self.delta=delta
        self.graph=graph
        self.path_iteration=path_iteration
        self.ant_amount=ant_amount
        self.starter_node=starter_node
        self.ant_amount=ant_amount
        self.pheromone_graph=self.graph.graph_pheromone

    def update_pheromones(self, ant):  #this function is meant to be executed once self.updated_pheromone_path is empty
        assert len(ant.unvisited_nodes) == 0
        path_size = len(ant.path)
        ant.graph.graph_pheromone *= ant.decay
        for node_index in range(ant.path[:-1]):
            ant.graph.graph_pheromone[node_index][node_index+1]+=ant.delta/path_size

    def generate_ant_list(self, starter_node, ant_amount):
        self.ant_list=[Ant(starter_node, self.graph, starter_node, self.delta) for x in range(ant_amount)]

    def find_path(self): #finds the most interesting path found by ants in ant_list, then returns its length and its pattern
        self.generate_ant_list(self.starter_node, self.ant_amount)
        ant_with_shortest_path=None
        shortest_path_found=np.inf
        for ant_index, ant in enumerate(self.ant_list):
            ant.path = ant.complete_path()
            if ant.path_length<shortest_path_found:
                ant_with_shortest_path=ant_index
                shortest_path_found = ant.path_length
        return shortest_path_found, self.ant_list[ant_with_shortest_path].path


    def find_shortest_path(self): #main function
        shortest_path_length=np.inf
        shortest_path=[]
        for _ in range(self.path_iteration):
            current_path_length, current_path=self.find_path()
            print("current path : ", current_path, "associated length : ", current_path_length)
            if current_path_length<shortest_path_length:
                shortest_path_length=current_path_length
                shortest_path=current_path
        return shortest_path_length,shortest_path
