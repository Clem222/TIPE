import numpy as np
import matplotlib.pyplot as plt
import random
import networkx as nx
from graph import Graph
from swarm import Swarm
from ant import Ant
import json

alphabetic_string='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#generate node edge value
def generate_node_edges_value(zero_value_proba, interval):
    if random.uniform(0,1) < zero_value_proba:
        return 0
    else: return random.randint(interval[0], interval[1])

#algorithm parameters
delta=3
decay=0.7
batch_size=10
iterations=5
graph_height=5

#graph variables
path_length_interval=(1,10)
graph_width=graph_height
nodes_name=alphabetic_string[0:graph_width*graph_height] #supposing that there are less than 26 nodes
zero_probability=0

#manages to generate or to keep the previous graph
new_graph_request =  input("generate graph ? ").lower()
if new_graph_request=='y' or new_graph_request=='yes' or new_graph_request=='oui' or new_graph_request=='o':
    main_graph = Graph([generate_node_edges_value(zero_probability, path_length_interval) if node%graph_width>node//graph_width
                        else -1\
                        for node in range(graph_height*graph_width)], [x for x in range(graph_height+1)], graph_height, graph_width)
    with open('graph.json', 'w') as file:
        json.dump(main_graph.graph.tolist(), file)
        file.close()
else:
    with open('graph.json', 'r') as file:
        main_graph = Graph(json.load(file), [x for x in range(graph_height+1)], graph_height, graph_width)
        file.close()

swarm=Swarm(main_graph, batch_size, 0, iterations, delta, decay)

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

path_length, path = swarm.find_shortest_path()
path_with_letters = [mapping[node] for node in path[0]]
print("chemin : ", path_with_letters, "\nLongueur du chemin : ", path_length)

#color the chosen path
for subpath_index, subpath in enumerate(path_with_letters[:-1]):
    nx.draw_networkx_edges(Gnx, pos, edgelist=[(path_with_letters[subpath_index], path_with_letters[subpath_index+1])], edge_color='red', width=2, alpha=0.6)

#show graph
plt.title("Graphe avec distances", fontsize=16)
plt.axis('off')
plt.tight_layout()
plt.show()

