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


def dejkstra(G,start):
    shortest_path = {vertex:float('+inf') for vertex in G }
    shortest_path[start] = 0
    queue = [start]
    while queue:
        current = queue.pop(0)
        for neighbour in G[current]:
            offering_shortest_path = shortest_path[current] + G[current][neighbour]
            if offering_shortest_path < shortest_path[neighbour]:
                shortest_path[neighbour] = offering_shortest_path
                queue.append(neighbour)
    return shortest_path

start_fruit = input()
print(dejkstra(G,start_fruit))