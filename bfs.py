import networkx as nx
import matplotlib.pyplot as plt
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


def get_bfs_tree(G, initial, fired ):
    fired.add(initial)
    queue = [initial]
    Y = nx.Graph()
    while queue:
        current = queue.pop(0)
        for neighbour in G[current]:
            if neighbour not in fired:
                Y.add_edge(current, neighbour, weight = G[current][neighbour])
                fired.add(neighbour)
                queue.append(neighbour)
    return Y

fired = set()
Y = get_bfs_tree(G, 'Orange',fired)
pos = nx.spring_layout(Y)
nx.draw_networkx_nodes(Y ,pos,node_size=70)
nx.draw_networkx_edges(Y, pos, edge_color='g',width=4)

nx.draw_networkx_labels(Y, pos,font_size=3,font_family='sans-serif')
plt.axis('off')
plt.savefig("graph3.png")
plt.show()
