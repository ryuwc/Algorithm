import sys

N = int(sys.stdin.readline().strip())
xy = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    xy.append((x, y))

xy.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(*xy[i])