import sys; sys.stdin = open('input_세제곱근.txt', 'r')

for tc in range(int(input())):
    N = int(input())

    result = round(N ** (1/3))
    if result ** 3 != N:
        result = -1
    print(f'#{tc+1}', result)