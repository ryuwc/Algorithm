import sys; sys.stdin = open('input_소인수분해.txt', 'r')

for tc in range(int(input())):
    num = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    while num != 1:
        if num % 11 == 0:
            num = num//11
            e += 1
        elif num % 7 == 0:
            num = num//7
            d += 1
        elif num % 5 == 0:
            num = num//5
            c += 1
        elif num % 3 == 0:
            num = num//3
            b += 1
        elif num % 2 == 0:
            num = num//2
            a += 1
    print(f'#{tc+1}', a, b, c, d, e)