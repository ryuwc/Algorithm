import sys; sys.stdin = open('sample_input_전기카트.txt', 'r')

# swea 5189 전기카트

def dfs(now, s):
    global result
    if 0 not in visited:
        if result > s:
            result = s
        return
    elif s > result:
        return
    for next in range(N):
        if next == now: continue                    # 가려는 곳이 현재위치면 x
        if visited[next]: continue                  # 이미 방문한 곳은 x

        # 가려는 곳이 출발지면 다른 모든곳을 방문했어야함
        if next == 0 and 0 in visited[1:]: continue
        visited[next] = 1
        dfs(next, s+arr[now][next])
        visited[next] = 0



for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0xff
    visited = [0] * N
    dfs(0, 0)
    print(f'#{tc+1}', result)



