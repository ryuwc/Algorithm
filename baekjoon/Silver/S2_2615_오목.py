import sys

# def solve():
#     for i in range(19):
#         for j in range(19):
#             if omok[i][j] == 1:
#                 for k in range(4):
#                     sums = 0
#                     for l in range(19):
#                         nr, nc = i + dr[k] * l, j + dc[k] * l
#                         if 0 <= nr < 19 and 0 <= nc < 19:
#                             if omok[nr][nc] == 1:
#                                 sums += 1
#                             elif omok[nr][nc] == 2 or omok[nr][nc] == 0:
#                                 break
#                     if sums == 5:
#                         nr, nc = i + r_dr[k], j + r_dc[k]
#                         if 0 <= nr < 19 and 0 <= nc < 19:
#                             if omok[nr][nc] == 0:
#                                 print(1)
#                                 print(i + 1, j + 1)
#                                 return
#
#
#             elif omok[i][j] == 2:
#                 for k in range(4):
#                     sums = 0
#                     for l in range(19):
#                         nr, nc = i + dr[k] * l, j + dc[k] * l
#                         if 0 <= nr < 19 and 0 <= nc < 19:
#                             if omok[nr][nc] == 2:
#                                 sums += 1
#                             elif omok[nr][nc] == 2 or omok[nr][nc] == 0:
#                                 break
#                     if sums == 5:
#                         nr, nc = i + r_dr[k], j + r_dc[k]
#                         if 0 <= nr < 19 and 0 <= nc < 19:
#                             if omok[nr][nc] == 0:
#                                 print(2)
#                                 print(i + 1, j + 1)
#                                 return
#
#     return print(0)

N = 19
omok = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dr = [1, 1, 0, -1]
dc = [0, 1, 1, 1]

def solve():
    for i in range(N):
        for j in range(N):
            if omok[i][j]:
                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    sums = 1

                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        continue
                    while 0 <= nr < N and 0 <= nc < N and omok[nr][nc] == omok[i][j]:
                        sums += 1
                        if sums == 5:
                            if 0 <= nr + dr[k] < N and 0 <= nc + dc[k] < N and omok[nr + dr[k]][nc + dc[k]] == omok[i][j]:
                                break
                            if 0 <= i - dr[k] < N and 0 <= j - dc[k] < N and omok[i - dr[k]][j - dc[k]] == omok[i][j]:
                                break
                            print(omok[i][j])
                            print(i + 1, j + 1)
                            return
                        nr += dr[k]
                        nc += dc[k]
    return print(0)

solve()
