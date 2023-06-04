import sys


def main():
    N, M = map(int, sys.stdin.readline().strip().split())
    prices = list()

    max_price = 0
    max_profit = 0

    for _ in range(M):
        prices.append(int(sys.stdin.readline().strip()))
    prices = sorted(prices, reverse=True)

    for idx, price in enumerate(prices):
        if (idx+1) > N:
            break
        tmp_profit = price * (idx + 1)
        if max_profit < tmp_profit:
            max_profit = tmp_profit
            max_price = price

    print(max_price, max_profit)


if __name__ == '__main__':
    main()