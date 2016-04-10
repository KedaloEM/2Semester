n, m = list(map(int, input().split()))

d = {}
for key in range(2*n):
    d[key] = []
for i in range(m):
    key, value = list(map(int,input().split()))
    d[key].append(value)
ar = [[0]*n for y in range(n)]
for r in range(n+1):
    if d[r]!=[]:
        for f in d[r]:
            ar[r-1][f-1] = 1
for q in range(n):
    for j in ar[q]:
        print(j, end=' ')
    print()




