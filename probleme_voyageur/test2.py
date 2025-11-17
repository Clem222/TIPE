import networkx as nx 
import numpy as np
import matplotlib.pyplot as plt

A = np.array([[0,1,0,1,0,0,0,0,0,0],

              [1,0,1,0,0,0,0,0,0,0],

              [0,0,0,1,1,0,0,0,0,0],

              [0,1,0,0,2,0,0,0,0,0],

              [0,0,1,1,0,0,0,0,0,0],

              [0,1,0,1,200,0,0,0,0,0],

              [0,0,1,1,1,0,0,0,0,0],

              [0,0,1,1,1,0,0,0,0,0],

              [0,1,0,1,2,1,0,0,0,0],

              [0,1,0,2,1,0,1,0,0,0]])

dic= {0:"A", 1:"B", 2:"C",3 :"D",4 :"E",5 :"F",6 :"G",7 :"H",8 :"I",9 :"J"}
G = nx.from_numpy_array(A)
G = nx.relabel_nodes(G, dic)
G.add_edge("A", "B", weight=3)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw(G, with_labels=True, font_size=10)
plt.show()
