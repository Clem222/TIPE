import numpy as np

#Ant class
class Ant:
    def __init__(self, starter_node, graph, current_node, delta=1, decay=0.9):
        self.graph=graph
        self.starter_node=starter_node
        self.current_node=current_node
        self.node_list=self.graph.node_list
        self.delta=delta
        self.decay=decay
        self.path = [self.starter_node]
        self.path_length=0
        self.graph_length = len(self.node_list)
        self.unvisited_nodes = set(self.node_list)-{self.current_node}
        self.is_active=True

    def get_pheromone_level(self, node_in, node_out): #returns pheromone levels in a single subpath
        return self.graph.graph_pheromone[node_in][node_out]

    def get_subpath_length(self, node_in, node_out): #returns subpath length
        return self.graph.graph[node_in][node_out]

    def chose_next_node(self, current_node:int):  #chose the next node, considering the pheromones and the length of the path
        probabilities={}
        for neightbor_node in range(len(self.graph.graph[current_node])):
            if neightbor_node in self.unvisited_nodes:
                subpath_length = self.get_subpath_length(self.current_node, neightbor_node)
                probabilities[neightbor_node]=float(self.get_pheromone_level(self.current_node, neightbor_node))**2/ \
                                                  float((subpath_length if subpath_length else 1))
        values = list(probabilities.values())
        total = sum([value if np.isfinite(value) else 0 for value in values])
        if total==0:
            return self.starter_node
        proba_array = np.array([values[x]/total if np.isfinite(values[x]) else 0 for x in range(len(probabilities))])
        keys = np.array(list(probabilities.keys()))
        choice = np.random.choice(keys, p=proba_array)
        return choice
        #returns the chosen node

    def move(self): #moves toward the most interesting path, then update pheromones on the graph
        most_optimal_node=self.chose_next_node(self.current_node)
        if most_optimal_node==None:
            self.path=[np.inf]
            self.is_active = False
        self.path.append(int(most_optimal_node))
        self.path_length += int(self.get_subpath_length(self.current_node, most_optimal_node))
        self.current_node=most_optimal_node
        if most_optimal_node != self.starter_node:
            self.unvisited_nodes.remove(int(most_optimal_node))
        else:
            self.unvisited_nodes={}

    def complete_path(self): #travels through the whole graph in a single path
        while self.unvisited_nodes:
            self.move()
        return self.path, self.path_length

