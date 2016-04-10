n = int(input())
G = {}
R = {}
for i in range(n):
    a, b = [x for x in input().split()]
    if a not in G:
        G[a] = []
    if b not in G:
        G[b] = []
    G[a].append(b)
    G[b].append(a)
    R[a] = 0
    R[b] = 0
for key in G:
    for f in G[key]:
        R[f] += 1
s = [key for key in R]
s = sorted(s)



w = 0
for key in R:
    if R[key]%2 ==1:
        print('NO')
        exit()
print('YES')

