import sys

N, K = map(int, sys.stdin.readline().split())
tmp = list(map(int, sys.stdin.readline().split()))
lst = []
lst.append(sum(tmp[:K]))

result = -0xfffffff
for i in range(0, N-K):
    lst.append(lst[i] - tmp[i] + tmp[K+i])

lst.sort()

print(lst[-1])