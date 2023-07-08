import sys


def flip(r, c):
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            ori[i][j] = 1 - ori[i][j]


def solve():
    cnt = 0
    for i in range(0, N - 2):
        for j in range(0, M - 2):
            if ori[i][j] != tar[i][j]:
                cnt += 1
                flip(i, j)

    if ori != tar:
        print(-1)
    else:
        print(cnt)


N, M = map(int, sys.stdin.readline().strip().split())
ori = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
tar = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

solve()
