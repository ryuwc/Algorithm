import sys; sys.stdin = open('4881.txt', 'r')

def perm(k, cur_sum):
    global ans
    if cur_sum >= ans:   # 가지치기, 가장 좋은 값을 찾았는데, 그 값보다 크면 다시 뒤로 리턴
        return

    if k == N:
        # for i in range(N):
        #     S += arr[i][cols[i]]
        # print(cols, S, cur_sum)
        if ans > cur_sum:
            ans = cur_sum
    else:
        for i in range(k, N):
            cols[k], cols[i] = cols[i], cols[k]     # k행의 열의 위치를 선택
            perm(k+1, cur_sum + arr[k][cols[k]])
            cols[k], cols[i] = cols[i], cols[k]

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cols = [i for i in range(N)]  # [0, 1, 2....., N-1]

    ans = 0xffffffff
    perm(0, 0)
    print(f'#{tc+1}', ans)
