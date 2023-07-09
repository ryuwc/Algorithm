import sys
from heapq import heappush, heappop

# sys.stdin = open('1927.txt', 'r')

N = int(sys.stdin.readline().strip())
lst = []

for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x:
        heappush(lst, x)
    else:
        print(heappop(lst)) if len(lst) else print(0)
