import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.Graph()
e = [('a', 'b', 0.3), ('b', 'c', 0.9), ('a', 'c', 0.5), ('c', 'd', 1.2)]
G.add_weighted_edges_from(e)
nx.draw(G)
plt.show()
