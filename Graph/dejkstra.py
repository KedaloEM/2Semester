import networkx as nx
import matplotlib.pyplot as plot


def dejkstra(G,start):
    shortest_path = {vertex:float('+inf') for vertex in G }
    shortest_path[start] = 0
    queue = [start]
    while queue:
        current = queue.pop(0)
        for neighbour in G[current]:
            offering_shortest_path = shortest_path[current] + G[current][neighbour]["weight"]
            if offering_shortest_path < shortest_path[neighbour]:
                shortest_path[neighbour] = offering_shortest_path
                queue.append(neighbour)
    return shortest_path

file = open('graph.txt' , 'r')
G = nx.Graph()
for line in file.readlines():
    a, b, weight = line.split()
    a, b, weight = str(a), str(b), int(weight)
    G.add_edge(a, b, weight=weight)


def shortest_path(G,first,last):
    way=nx.Graph()
    d = 0
    friend = [last]
    dejks = dejkstra(nx.to_dict_of_dicts(G), first)
    while len(friend) !=0:
        for neighbour in G[last]:
            if d == 0:
                if G[last][neighbour]['weight'] == (dejks[last] - dejks[neighbour]):
                    way.add_edge(last, neighbour, weight = G[last][neighbour]['weight'])
                    friend.append(neighbour)
                    d = 1
                    if neighbour ==first:
                        return way
        d = 0
        last = friend.pop(-1)
first,last = input().split()
way = shortest_path(G,first,last)
pos = nx.spring_layout(way, iterations=1)
nx.draw(way, pos)
nx.draw_networkx_edge_labels(way, pos)
nx.draw_networkx_labels(way,pos,font_size=7,font_family='sans-serif')
way1 = nx.to_dict_of_dicts(way)
summary = 0
for neighbour in way1:
    for neighbour1 in way1[neighbour]:
        summary+=way1[neighbour][neighbour1]['weight']
print(summary/2)
plot.show()




