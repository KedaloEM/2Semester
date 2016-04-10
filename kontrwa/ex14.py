import pprint
G = eval(input())
R = {}
for key in G:
    R[key] = set()
for key in G:
    for f in G[key]:
        R[f].add(key)
pprint.pprint(R)