

def dejkstra(G,start):
    shortest_path = {vertex:float('+inf') for vertex in G }
    shortest_path[start] = 0
    queue = [start]
    while queue:
        current = queue.pop(0)
        for neighbour in G[current]:
            offering_shortest_path = shortest_path[current] + 1
            if offering_shortest_path < shortest_path[neighbour]:
                shortest_path[neighbour] = offering_shortest_path
                queue.append(neighbour)
    return shortest_path

G = {}
n = int(input())
for i in range(n):
    a, b = [x for x in input().split()]
    if a not in G:
        G[a] = []
    if b not in G:
        G[b] = []
    G[a].append(b)
x = input()
s = [key for key in G]
s = sorted(s)
short = dejkstra(G,x)
for key in s:
    if short[key]!=float('+inf'):
        print(key, short[key])
    else:
        print(key, -1)