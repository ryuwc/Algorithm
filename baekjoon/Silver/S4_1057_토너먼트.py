import sys


def make_new_num(num):
    if num % 2 == 1:
        return num // 2 + 1
    return num // 2


def is_same_round(num1, num2):
    return (num1 - 1) // 2 == (num2 - 1) // 2


def main():
    N, kim, lim = map(int, sys.stdin.readline().strip().split())

    cnt = 1
    while not is_same_round(kim, lim):
        kim = make_new_num(kim)
        lim = make_new_num(lim)
        cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
