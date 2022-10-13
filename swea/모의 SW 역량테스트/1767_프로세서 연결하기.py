# import sys; sys.stdin = open('input_프로세서.txt', 'r')

D = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# cnt와 length를 리턴해주는 함수
def cnt_length():
    # arr을 깊은 복사
    tmp = [i[:] for i in arr]
    cnt = 0
    length = 0
    for i in range(Q_len):
        # 방향이 없을 때는 continue
        if Q_dir[i] < 0:
            continue
        # 그 방향대로 가다가 1을 만나면 continue
        if not check(Q[i][0], Q[i][1], Q_dir[i], tmp):
            continue
        # 프로세서 연결이 가능한 코어임 코어 + 1
        cnt += 1
        di = Q[i][0] + D[Q_dir[i]][0]
        dj = Q[i][1] + D[Q_dir[i]][1]
        # 경계를 벗어 날 때 까지
        while 0 <= di < N and 0 <= dj < N:
            # 그 방향대로 쭉 1을 이어붙여주고 length를 증가
            tmp[di][dj] = 1
            length += 1
            di += D[Q_dir[i]][0]
            dj += D[Q_dir[i]][1]
    return cnt, length

def solve(idx):
    global max_cnt, min_len

    if idx == Q_len:
        cnt, length = cnt_length()
        if cnt > max_cnt:
            max_cnt = cnt
            min_len = length
        elif cnt == max_cnt:
            min_len = min(min_len, length)
        return

    # flag가 False면 해당 코어는 네 방향 모두 갈 수 다는 뜻
    flag = False
    for d in range(4):
        if check(Q[idx][0], Q[idx][1], d, arr):
            flag = True
            Q_dir[idx] = d
            solve(idx + 1)
    if not flag:
        Q_dir[idx] = -1
        solve(idx + 1)

# 행, 열, 방향을 받고 그 방향대로 쭉 가다가 1을 만나면 Flase를 리턴, 경계를 벗어나면 연결 가능 True를 리턴
def check(i, j, d, arr):
    di = i + D[d][0]
    dj = j + D[d][1]
    while 0 <= di < N and 0 <= dj < N:
        if arr[di][dj] == 1:
            return False
        di += D[d][0]
        dj += D[d][1]
    return True

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Q = []

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if arr[i][j] == 1:
                Q.append([i, j])

    Q_len = len(Q)
    Q_dir = [0] * Q_len
    max_cnt = 0
    min_len = 9e9

    solve(0)

    print(f'#{tc+1}', min_len)