import sys

N = int(sys.stdin.readline())

S = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num > 0:
        S.append(num)
    elif num == 0:
        S.pop()

print(sum(S))