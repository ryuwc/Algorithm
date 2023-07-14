import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
target = list(map(int, sys.stdin.readline().split()))
dic = defaultdict(int)

for num in cards:
    dic[num] += 1

for i in range(M):
    print(dic[target[i]], end=' ')


