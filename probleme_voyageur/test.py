import igraph
import numpy as np
A = np.array([1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,1]) ; A=A.reshape(4,4) # 4 objets

A = list(A)

g = igraph.Graph.Adjacency(A,mode=igraph.ADJ_UNDIRECTED)

obj = igraph.plot(g,vertex_label_size=15,vertex_size=35,vertex_color='#ffe4c4')

obj.show()
