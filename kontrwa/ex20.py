used = set()
def svyaz(G,start):
    global used
    if start not in used:
        used.add(start)
    for neighbour in G[start]:
        if neighbour not in used:
            used.add(neighbour)
            svyaz(G,neighbour)
    return(used)



k = 1
G = {}
n = int(input())
a, b = [x for x in input().split()]
G[a] = []
G[b] = []
G[a].append(b)
G[b].append(a)
y = a
for i in range(n-1):
    a, b = [x for x in input().split()]
    if a not in G:
        G[a] = []
    if b not in G:
        G[b] = []
    G[a].append(b)
    G[b].append(a)

svyaz(G, y)
for key in G:
    if key not in used:
        k+=1
        svyaz(G,key)
print(k)
