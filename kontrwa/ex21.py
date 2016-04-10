R = {}
used  = []

def get_dfs_tree(G,initial):
    global R
    queue = [initial]
    used = {initial}
    R[initial] = None
    while queue:
        top = queue.pop(0)
        for m in G[top]:
            if m not in used:
                if m not in R:
                    R[m] = None
                R[m] = top
                used.add(m)
                queue.append(m)
    return(R)



G = {}
n = int(input())
for i in range(n):
    a, b = [x for x in input().split()]
    if a not in G:
        G[a] = []
    if b not in G:
        G[b] = []
    G[a].append(b)
initial = input()
print(get_dfs_tree(G,initial))

