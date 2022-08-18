import sys

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

result = 0
for i in range(N-2):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if cards[i] + cards[j] + cards[k] <= M and cards[i] + cards[j] + cards[k] > result:
                result = cards[i] + cards[j] + cards[k]
            else:
                continue
print(result)

