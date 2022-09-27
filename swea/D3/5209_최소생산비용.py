import sys; sys.stdin = open('5209.txt')

def solve(depth, sums):
    global rst
    # depth가 N이 되면 return
    if depth == N:
        rst = min(rst, sums)
        return
    # 가지치기
    if sums >= rst:
        return
    # visit체크 확인 하고 안갔으면 ㄱㄱ
    # 같은 행과 열을 가지지않음
    for i in range(N):
        if visit[i]:
            continue
        visit[i] = 1
        solve(depth+1, sums+fac[depth][i])
        visit[i] = 0

for tc in range(int(input())):
    N = int(input())
    fac = [list(map(int, input().split())) for _ in range(N)]

    rst = 1e9
    visit = [0] * (N)
    solve(0, 0)
    print(f'#{tc+1}', rst)
