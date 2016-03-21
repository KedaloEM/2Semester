import networkx as nx
import matplotlib.pyplot as plt



def get_dfs_tree(G,initial):
    queue = [initial]
    Q = nx.Graph()
    used = {initial}
    while queue:
        top = queue.pop(0)
        for m in G[top]:
            if m not in used:
                used.add(m)
                Q.add_edge(top, m, weight = G[top][m])
                queue.append(m)
    return (Q)


file = open('graph.txt' , 'r')
G = {}
for line in file.readlines():
    a ,b, weight = line.split()
    a, b, weight = str(a), str(b), int(weight)
    if a not in G:
        G[a] = {b:weight}
    else:
        G[a][b] = weight
    if b not in G:
        G[b] = {a:weight}
    else:
        G[b][a] = weight
Q = get_dfs_tree(G,'Orange')
pos = nx.spring_layout(Q)
nx.draw_networkx_nodes(Q ,pos,node_size=70)
nx.draw_networkx_edges(Q, pos, edge_color='b',width=4)
nx.draw_networkx_labels(Q, pos,font_size=3,font_family='sans-serif')
plt.axis('off')
plt.savefig("graph2.png")
plt.show()