import sys

N, K = map(int, sys.stdin.readline().strip().split())
result = 1
for i in range(K):
    result *= N - i
for i in range(1, K + 1):
    result //= i
print(result)