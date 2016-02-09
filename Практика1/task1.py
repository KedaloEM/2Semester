import sys
x = 0
for arg in sys.argv:
    if len(arg)%3 == 0:
        x += 1
print(x)