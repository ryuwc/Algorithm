import sys


def main():
    N, M = map(int, sys.stdin.readline().strip().split())
    prices = sorted([int(sys.stdin.readline().strip()) for _ in range(M)], reverse=True)

    max_profit = max_price = 0
    for idx, price in enumerate(prices[:N], 1):
        tmp_profit = price * idx
        if max_profit < tmp_profit:
            max_profit = tmp_profit
            max_price = price

    print(max_price, max_profit)


if __name__ == '__main__':
    main()
