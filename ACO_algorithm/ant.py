import numpy as np


#Ant class
class Ant:
    def __init__(self, starter_node, graph, current_node, delta):
        self.graph=graph
        self.starter_node=starter_node
        self.current_node=current_node
        self.node_list=self.graph.node_list
        self.pheromone_amount=delta
        self.path = [self.starter_node]
        self.path_length=0
        self.graph_length = len(self.node_list)
        self.updated_pheromone_path= set()
        self.unvisited_nodes = set(self.node_list)-{self.current_node}
        self.added_pheromones=np.zeros_like(self.graph.graph_pheromone, dtype=(np.float64()))

    def get_pheromone_level(self, node_in, node_out): #returns pheromone levels in a single subpath
        return self.graph.graph_pheromone[node_in][node_out]

    def get_subpath_length(self, node_in, node_out): #returns subpath length
        return self.graph[node_in][node_out]

    def chose_next_node(self, current_node:int):
        probabilities={}
        print(self.graph.graph(current_node)) #TODO fix zat
        for neightbor_node in range(self.graph.graph[current_node]):
            if neightbor_node>0:
                probabilities[neightbor_node]=self.get_pheromone_level(self.current_node, neightbor_node)**2/\
                                    self.get_subpath_length(self.current_node, neightbor_node)
        return np.random.choice(probabilities.keys(),p=np.array(probabilities.values())/sum(probabilities.values()))
        #returns the chosen node

    def move(self): #moves toward the most interesting path, then update pheromones on the graph
        '''
        most_optimal_node=min([self.get_pheromone_level(self.current_node, adjacent_node)**2/\
                                    self.get_subpath_length(self.current_node, adjacent_node) \
                                    for adjacent_node in self.graph.graph[self.current_node]])
        '''
        most_optimal_node=self.chose_next_node(self.current_node)
        self.path.append(most_optimal_node)
        self.path_length += self.get_subpath_length(self.current_node, most_optimal_node)
        self.update_pheromones(self.current_node, most_optimal_node)
        self.current_node=most_optimal_node

    def complete_path(self): #travels through the whole graph in a single path
        while self.unvisited_nodes:
            self.move()
        return self.path, self.path_length

    def update_pheromones(self, node_in, node_out):
        self.graph.graph_pheromone[node_in][node_out]+=self.pheromone_amount
        self.updated_pheromone_path.add((node_in, node_out))
