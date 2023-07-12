import sys

N = int(sys.stdin.readline().strip())
lst = []
for i in range(N):
    a, b = sys.stdin.readline().strip().split()
    a = int(a)
    lst.append([a, i, b])
lst.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    print(lst[i][0], lst[i][2])
