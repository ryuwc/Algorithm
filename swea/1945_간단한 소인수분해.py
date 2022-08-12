
T = int(input())
for tc in range(1, T+1):
    num = int(input())
    count_2 = 0
    count_3 = 0
    count_5 = 0
    count_7 = 0
    count_11 = 0
    while True:
        while True:
            if num % 11 == 0:
                num = num / 11
                count_11 += 1
            elif num == 1:
                break
            else:
                break
        while True:
            if num % 7 == 0:
                num = num / 7
                count_7 += 1
            elif num == 1:
                break
            else:
                break
        while True:
            if num % 5 == 0:
                num = num / 5
                count_5 += 1
            elif num == 1:
                break
            else:
                break
        while True:
            if num % 3 == 0:
                num = num / 3
                count_3 += 1
            elif num == 1:
                break
            else:
                break
        while True:
            if num == 1:
                break
            num = num/2
            count_2 += 1
        break
    print(f'#{tc}', count_2, count_3, count_5, count_7, count_11)
