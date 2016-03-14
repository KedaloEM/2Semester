__author__ = 'student'
import networkx as nx
import matplotlib.pyplot as plt
file = open('graph.txt' , 'r')
G = nx.Graph()
D = {}
for line in file.readlines():
    a ,b, weight = line.split()
    a, b, weight = str(a), str(b), int(weight)
    if a not in D:
        D[a] = {b:weight}
    else:
        D[a][b] = weight
    if b not in D:
        D[b] = {a:weight}
    else:
        D[b][a] = weight
    G.add_edge(a, b, weight = weight)
pos = nx.spectral_layout(G)
elarge = [(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=200]
esmall = [(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >=200]
nx.draw_networkx_nodes(G,pos,node_size=3000)
nx.draw_networkx_edges(G,pos, edgelist=elarge, edge_color='y',width=4)
nx.draw_networkx_edges(G,pos, edgelist=esmall, edge_color='b',width=4, style = 'dashed')


nx.draw_networkx_labels(G,pos,font_size=14,font_family='sans-serif')
plt.axis('off')
plt.savefig("graph1.png")
plt.show()


G.dict = nx.to_dict_of_dicts(G)


def get_dfs_tree(G,initial):
    queue = [initial]
    Q = nx.Graph()
    used = {initial}
    while queue:
        top = queue.pop(0)
        for m in G[top]:
            if m not in used:
                used.add(m)
                Q.add_edge(top, m, weight = G[top][m]['weight'])
                queue.append(m)
    return (Q,used)
Q = get_dfs_tree(G.dict,'Apple',)

nx.draw_networkx_nodes(Q ,pos,node_size=3000)
nx.draw_networkx_edges(Q, pos, edge_color='b',width=4)

nx.draw_networkx_labels(Q, pos,font_size=14,font_family='sans-serif')
plt.axis('off')
plt.savefig("graph2.png")
plt.show()



def get_bfs_tree(G, initial, fired ):
    fired.add(initial)
    queue = [initial]
    Y = nx.Graph()
    while queue:
        current = queue.pop(0)
        for neighbour in G[current]:
            if neighbour not in fired:
                Y.add_edge(current, neighbour, weight = G[current][neighbour]['weight'])
                fired.add(neighbour)
                queue.append(neighbour)
    return Y

fired = set()
Y = get_bfs_tree(G.dict, 'Apple',fired)

nx.draw_networkx_nodes(Y ,pos,node_size=3000)
nx.draw_networkx_edges(Y, pos, edge_color='g',width=4)

nx.draw_networkx_labels(Y, pos,font_size=14,font_family='sans-serif')
plt.axis('off')
plt.savefig("graph3.png")
plt.show()









