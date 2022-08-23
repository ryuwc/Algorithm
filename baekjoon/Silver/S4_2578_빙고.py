# import sys; sys.stdin = open('input_빙고.txt', 'r')

bingo = [list(map(int, input().split())) for _ in range(5)]
nums = list(map(int, input().split()))
for _ in range(4):
    nums += list(map(int, input().split()))


dr = [1, 1]
dc = [1, -1]

def func():
    count = 0
    for num in nums:
        for i in range(5):
            for j in range(5):
                bingo_sum = 0
                if num == bingo[i][j]:
                    bingo[i][j] = 0
                    count += 1
                    for k in range(5):
                        r_num = 0
                        for l in range(5):
                            if bingo[k][l] != 0:
                                break
                            else:
                                if bingo[k][l] == 0:
                                    r_num += 1
                        if r_num == 5:
                            bingo_sum += 1
                            if bingo_sum == 3:
                                return count
                    for l in range(5):
                        c_num = 0
                        for k in range(5):
                            if bingo[k][l] != 0:
                                break
                            else:
                                if bingo[k][l] == 0:
                                    c_num += 1
                        if c_num == 5:
                            bingo_sum += 1
                            if bingo_sum == 3:
                                return count
                    r = c = 0
                    if bingo[r][c] == 0:
                        cross1 = 0
                        for k in range(5):
                            nr, nc = r + dr[0]*k, c + dc[0]*k
                            if bingo[nr][nc] == 0:
                                cross1 += 1
                        if cross1 == 5:
                            bingo_sum += 1
                            if bingo_sum == 3:
                                return count
                    r, c = 0, 4
                    if bingo[r][c] == 0:
                        cross2 = 0
                        for k in range(5):
                            nr, nc = r + dr[1]*k, c + dc[1]*k
                            if bingo[nr][nc] == 0:
                                cross2 += 1
                        if cross2 == 5:
                            bingo_sum += 1
                            if bingo_sum == 3:
                                return count

print(func())