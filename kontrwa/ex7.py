import pprint
n = int(input())

G = {}
for i in range(n):
    a,b=[x for x in input().split()]
    if a not in G:
        G[a] = {b}
    else:
        G[a].add(b)
    if b not in G:
        G[b] = {a}
    else:
        G[b].add(a)
pprint.pprint(G)