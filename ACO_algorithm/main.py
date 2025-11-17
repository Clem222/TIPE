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
delta=1.5
decay=0.5
batch_size=30
iterations=20
node_amount=5

#graph variables
path_length_interval=(1,10)

def generate_name(index, output=""):
    if index==0:
        return output[::-1]
    else:
        return generate_name((index-1)//26, output+alphabetic_string[(index-1)%26])

nodes_name=[generate_name(x) for x in range(1,node_amount+1)]
print(nodes_name)
zero_probability=0

#manages to generate or to keep the previous graph
new_graph_request =  input("generate graph ? ").lower()
if new_graph_request=='y' or new_graph_request=='yes' or new_graph_request=='oui' or new_graph_request=='o':
    main_graph = Graph([generate_node_edges_value(zero_probability, path_length_interval) if node%node_amount>node//node_amount
                        else -1\
                        for node in range(node_amount**2)], [x for x in range(node_amount+1)], node_amount, node_amount)


    with open('graph.json', 'w') as file:
        json.dump(main_graph.graph.tolist(), file)
        file.close()
else:
    with open('graph.json', 'r') as file:
        main_graph = Graph(json.load(file), [x for x in range(node_amount+1)], node_amount, node_amount)
        file.close()

mapping={i: nodes_name[i] for i in range(len(nodes_name))}
reverse_mapping={mapping[i]:i for i in range(len(mapping))}
removed_subpath=[]
remove_subpath_request = input("remove subpath ?").lower()
while remove_subpath_request=='y' or remove_subpath_request=='yes' or remove_subpath_request=='oui' or remove_subpath_request=='o':
    input_node = input("input node : ").upper()
    output_node = input("output node : ").upper()
    if input_node==output_node:
        print("Mauvais format, veuillez choisir deux noeuds distincts")
        continue
    try:
        main_graph.remove_subpath(reverse_mapping[input_node], reverse_mapping[output_node])
        removed_subpath.append((input_node, output_node))
    except:
        print("Mauvais format, veuillez entrer des noeuds valides")
        continue
    remove_subpath_request = input("remove subpath ?").lower()
swarm=Swarm(main_graph, batch_size, 0, iterations, delta, decay)

#prepare graph
Gnx=nx.from_numpy_array(main_graph.graph)
Gnx=nx.relabel_nodes(Gnx, mapping)

#setup the figure
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(Gnx, seed=42, k=100)
nx.draw_networkx_nodes(Gnx, pos, node_color='lightblue', node_size=700, alpha=0.9)
nx.draw_networkx_edges(Gnx, pos, width=2, alpha=0.6)

#draw nodes
nx.draw_networkx_labels(Gnx, pos, font_size=12, font_weight='bold')

#show path length
edge_labels = nx.get_edge_attributes(Gnx, 'weight')
for subpath in removed_subpath:
    edge_labels[subpath]="chemin détruit"
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

