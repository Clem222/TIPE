import numpy as np
import matplotlib.pyplot as plt
import random
import networkx as nx
from graph import Graph
from swarm import Swarm
from ant import Ant

alphabetic_string='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#generate node edge value
def generate_node_edges_value(zero_value_proba, interval):
    if random.uniform(0,1) < zero_value_proba:
        return 0
    else: return random.randint(interval[0], interval[1])

#generate graph

#graph variables
path_length_interval=(1,10)
graph_height=5
graph_width=graph_height
nodes_name=alphabetic_string[0:graph_width*graph_height] #considering that there is less than 26 nodes
zero_probability=0

main_graph = Graph([generate_node_edges_value(zero_probability, path_length_interval) \
                    for node in range(graph_height*graph_width)], nodes_name, graph_height, graph_width)

test_swarm=Swarm(main_graph, 5, 0, 3, 2)
test_ant=Ant(0, main_graph, 0, 1.1)
#prepare graph
Gnx=nx.from_numpy_array(main_graph.graph)
mapping={i: nodes_name[i] for i in range(len(nodes_name))}
Gnx=nx.relabel_nodes(Gnx, mapping)


#setup the figure
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(Gnx, seed=42, k=2)
nx.draw_networkx_nodes(Gnx, pos, node_color='lightblue', node_size=700, alpha=0.9)
nx.draw_networkx_edges(Gnx, pos, width=2, alpha=0.6)

#draw nodes
nx.draw_networkx_labels(Gnx, pos, font_size=12, font_weight='bold')

#print path length
edge_labels = nx.get_edge_attributes(Gnx, 'weight')
nx.draw_networkx_edge_labels(Gnx, pos, edge_labels, font_size=10)

print(test_ant.complete_path())

#show graph
plt.title("Graphe avec distances", fontsize=16)
plt.axis('off')
plt.tight_layout()
plt.show()

