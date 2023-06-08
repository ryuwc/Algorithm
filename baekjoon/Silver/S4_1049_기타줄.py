import sys


def main():
    N, M = map(int, sys.stdin.readline().strip().split())

    min_set = 9e9
    min_one = 9e9

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().strip().split())
        min_set = min(min_set, a)
        min_one = min(min_one, b)

    all_set_price = (N // 6 + 1) * min_set if N % 6 else N // 6 * min_set
    all_one_price = min_one * N
    mix_price = (N // 6) * min_set + (N % 6) * min_one

    print(min(all_set_price, all_one_price, mix_price))


if __name__ == '__main__':
    main()
