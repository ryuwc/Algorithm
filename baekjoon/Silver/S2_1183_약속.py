import sys

def main():
    N = int(sys.stdin.readline().strip())
    dif = []
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().strip().split())
        dif.append(a - b)

    dif.sort()

    if N % 2 == 1:
        rst = 1
    else:
        rst = abs(dif[N // 2] - dif[N // 2 - 1]) + 1

    print(rst)

if __name__ == '__main__':
    main()
