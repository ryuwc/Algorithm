import sys


def solve():
    if N == 0:
        return print(0)

    fifty = round(N * 0.15 + 0.000001)

    print(round((sum((scores[fifty:N - fifty])) / (N - 2 * fifty) + 0.000001)))


N = int(sys.stdin.readline().strip())
scores = [int(sys.stdin.readline().strip()) for _ in range(N)]
scores.sort()

solve()


