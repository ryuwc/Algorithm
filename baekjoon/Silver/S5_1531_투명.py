import sys


def main():
    N, M = map(int, sys.stdin.readline().strip().split())

    paper = [[0] * 101 for _ in range(101)]

    for _ in range(N):
        lr, lc, hr, hc = map(int, sys.stdin.readline().strip().split())
        for i in range(lr, hr + 1):
            for j in range(lc, hc + 1):
                paper[i][j] += 1

    rst = 0
    for i in range(1, 101):
        for j in range(1, 101):
            if paper[i][j] > M:
                rst += 1

    print(rst)


if __name__ == '__main__':
    main()
