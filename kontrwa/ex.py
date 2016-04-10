import pprint
graph = eval(input())
for key in graph:
    for f in graph[key]:
        if key not in graph[f]:
            graph[f].add(key)
pprint.pprint(graph)
