__author__ = 'student'
import networkx as nx
import matplotlib.pyplot as plt

file = open('graph.txt' , 'r')
G = nx.Graph()
D = {}
for line in file.readlines():
    a ,b, weight = line.split()
    a, b, weight = str(a), str(b), int(weight)
    G.add_edge(a, b, weight = weight)


pos = nx.spring_layout(G, iterations=0)
elarge = [(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=200]
esmall = [(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >=200]
nx.draw_networkx_nodes(G,pos,node_size=300)
nx.draw_networkx_edges(G,pos, edgelist=elarge, edge_color='y',width=4)
nx.draw_networkx_edges(G,pos, edgelist=esmall, edge_color='b',width=4, style = 'dashed')
nx.draw_networkx_labels(G,pos,font_size=7,font_family='sans-serif')
plt.axis('off')
plt.savefig("graph1.png")
plt.show()









