import sys

N = int(sys.stdin.readline())
result = 0
for i in range(1, N+1):
    a = list(map(int, str(i)))
    sums = i + sum(a)
    if sums == N:
        result = i
        break

print(result)
