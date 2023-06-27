import sys; sys.stdin = open('5099.txt', 'r')
from collections import deque


def solve(N, pizzas):
    oven = deque(pizzas[:N])
    remain_pizzas = deque(pizzas[N:])
    while len(oven) != 1:
        idx, pizza = oven.popleft()
        pizza //= 2

        if pizza == 0:
            if remain_pizzas:
                oven.append(remain_pizzas.popleft())
        else:
            oven.append([idx, pizza])

    return oven[0][0]


def main():
    T = int(input())
    for tc in range(1, T+1):
        N, M = map(int, input().split())
        tmp_pizzas = list(map(int, input().split()))
        pizzas = []
        for idx, pizza in enumerate(tmp_pizzas):
            pizzas.append([idx+1, pizza])

        print(f'#{tc} {solve(N, pizzas)}')


if __name__ == '__main__':
    main()