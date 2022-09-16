import sys; sys.stdin = open('input_홈방범.txt', 'r')

# 길이가 k인 마름모의 비용을 구하는 함수
def cal_cost(k):
    return k*k + (k-1)*(k-1)

for tc in range(int(input())):
    N, M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    homes = []                  # 집이 있는 곳의 행과 열을 담을 리스트
    for i in range(N):
        for j in range(N):
            if maps[i][j]:      # 집이 있다면, 넣어준다.
                homes.append([i, j])

    max_home = 0
    for i in range(N):
        for j in range(N):
            # maps안에서의 최대 거리를 길이로, 길이 마다 집이 있는 경우를 넣어줄 리스트
            dist = [0] * (2*N)
            # 기준 점 i, j로 부터의 거리를 인덱스로 하여 넣어준다.
            for a, b in homes:
                dist[abs(i-a) + abs(j-b)] += 1
            # 카운팅 정렬을 할 때 처럼 병합해준다.
            for k in range(1, 2*N):
                dist[k] += dist[k-1]
            # 길이가 1부터 2N까지
            for k in range(1, 2*N):
                # 길이에 있는 집에 대해 적자를 보지 않는다면, max_home 변환
                if dist[k] * M - cal_cost(k+1) >= 0:    # cal_cost(k+1)인 이유는, 길이+1 = 마름모의 길이이기 때문
                    max_home = max(max_home, dist[k])

    print(f'#{tc+1}', max_home)
