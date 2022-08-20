import sys; sys.stdin = open('input_스도쿠검증.txt', 'r')

def checkcheck(sdoku):
    # box 검사
    for i in range(9):
        for j in range(9):
            if i % 3 == 0 and j % 3 == 0:
                sums = 0
                for k in range(3):
                    for l in range(3):
                        sums += sdoku[k][l]
                if sums != 45:
                    return 0

    # 행 검사
    for i in range(9):
        sums = 0
        for j in range(9):
            sums += sdoku[i][j]
        if sums != 45:
            return 0

    # 열 겸사
    for j in range(9):
        sums = 0
        for i in range(9):
            sums += sdoku[i][j]
        if sums != 45:
            return 0
    return 1


for tc in range(int(input())):
    sdoku = []
    for _ in range(9):
        sdoku += [list(map(int, input().split()))]

    print(f'#{tc+1}', checkcheck(sdoku))



