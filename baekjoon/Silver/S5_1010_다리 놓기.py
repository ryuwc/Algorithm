import sys


def main():
    TC = int(sys.stdin.readline().strip())
    for _ in range(TC):
        N, M = map(int, sys.stdin.readline().strip().split())

        rst = 1
        for i in range(M, M-N, -1):
            rst *= i
        for i in range(1, N+1):
            rst //= i

        print(rst)


if __name__ == '__main__':
    main()