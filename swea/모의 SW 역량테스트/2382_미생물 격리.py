import sys; sys.stdin = open('input_미생물.txt', 'r')

D = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]
RD = [0, 2, 1, 4, 3]

def moving():
    info_dict = {}
    for now in range(K):
        data = info[now]
        r, c, num, d = data
        if num == 0: continue
        nr, nc = r + D[d][0], c + D[d][1]
        data[0] = nr
        data[1] = nc
        if nr == 0 or nr == N - 1 or nc == 0 or nc == N - 1:
            data[2] //= 2
            data[3] = RD[d]

        if (nr, nc) not in info_dict:
            info_dict[(nr, nc)] = (now, num)
            continue

        pre_info = info_dict.get((nr, nc))
        pre_idx = pre_info[0]
        pre_num = pre_info[1]
        if num > pre_num:
            data[2] += info[pre_idx][2]
            info_dict[(nr, nc)] = (now, num)
            info[pre_idx][2] = 0
        else:
            info[pre_idx][2] += num
            data[2] = 0

for tc in range(int(input())):
    N, M, K = map(int, input().split())

    info = [list(map(int, input().split())) for _ in range(K)]

    for m in range(M):
        moving()

    result = 0
    for k in range(K):
        result += info[k][2]


    print(f'#{tc+1}', result)










