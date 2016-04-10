import pprint
t = 0
def obhod(G,top, Start, End):
    global t
    t+=1
    Start[top] = t

                Start[vertex] = t
            t+=1
            End[vertex] = t
            flag = True
            for vertex in G[top]:
                if vertex not in End:
                    flag = False
            if flag ==True:
                t +=1
                End[top] = t
            if top1!=None:
                t+=1
                End[top1] = t

    return End, Start


n = int(input())
G = {}
for i in range(n):
    a, b = [x for x in input().split()]
    if a not in G:
        G[a] = set()
    if b not in G:
        G[b] = set()
    G[a].add(b)
    G[b].add(a)

pprint.pprint(G)
End, Start = obhod(G,'A',Start = {},End = {} )
s = (key for key in Start)
s = sorted(s)
for key in s:
    print(key, Start[key])
print(End)