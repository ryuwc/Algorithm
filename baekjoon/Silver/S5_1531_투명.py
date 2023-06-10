import sys


def main():
    N, M = map(int, sys.stdin.readline().strip().split())

    paper = [[0] * 101 for _ in range(101)]

    for _ in range(N):
        lr, lc, hr, hc = map(int, sys.stdin.readline().strip().split())
        for i in range(lr, hr + 1):
            paper[i][lc:hc+1] = [j + 1 for j in paper[i][lc:hc+1]]

    rst = sum(1 for i in range(1, 101) for j in range(1, 101) if paper[i][j] > M)

    print(rst)


if __name__ == '__main__':
    main()
