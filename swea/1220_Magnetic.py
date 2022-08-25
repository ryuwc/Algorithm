import sys; sys.stdin = open('input_Magnetic.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for j in range(N):
        flag = 0
        for i in range(N):
            if magnetic[i][j] == 1:         # 열 우선 순회 하다가 1을 만나고
                if flag == 0 or flag == 2:  # flag가 0이나 2이면
                    flag = 1                # flag를 1로 바꿔줌
            elif magnetic[i][j] == 2:       # 그러고 2를 만나고
                if flag == 1:               # flag가 1이면
                    flag = 2                # flag를 2로 바꿔주고
                    cnt += 1                # cnt를 1증가, 교착 상태인 자석
            else:                           # 요소가 0일 떄
                if flag == 2:               # flag가 2라면
                    flag = 0                # flag를 0으로 바꿔줌
    print(f'#{tc}', cnt)


    # ti = 100
    # while ti:
    #     for p in range(N):
    #         for o in range(N):
    #             if magnetic[o][p] == 2 and magnetic[o+1][p] == 0:
    #                 magnetic[o][p] = 0
    #                 magnetic[o+1][p] = 2
    #             elif magnetic[o][p] == 1 and magnetic[o-1][p] == 0:
    #                 magnetic[o][p] = 0
    #                 magnetic[o-1][p] = 1
    #     ti -= 1
    #
    # sol = 0
    # for b in range(N):
    #     lst = []
    #     for a in range(N):
    #         if magnetic[a][b] == 2:
    #             lst.append(2)
    #         if magnetic[a][b] == 1 and lst:
    #             lst.clear()
    #             sol += 1
    # print(sol)







