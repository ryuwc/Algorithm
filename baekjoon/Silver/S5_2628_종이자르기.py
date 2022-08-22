import sys; sys.stdin = open('input_종이자르기.txt', 'r')

M, N = map(int, input().split())
r = [0, N]
c = [0, M]
K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    if a == 0:
        r.append(b)
    else:
        c.append(b)
r.sort()
c.sort()

result = 0
for i in range(1, len(r)):
    for j in range(1, len(c)):
        h = r[i] - r[i-1]
        w = c[j] - c[j-1]
        result = max(result, w*h)
print(result)


