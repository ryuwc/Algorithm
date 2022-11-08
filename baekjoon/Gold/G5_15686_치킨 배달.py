import sys

def solve(m, index):
    global rst

    # 치킨집을 최대로 골랐으면 모든 집에 대해 치킨 집과의 거리를 계산한다.
    if m == M:
        cnt = 0
        for home in homes:
            r, c = home[0], home[1]
            tmp = 2*N+1
            for chick in ans:
                er, ec = chick[0], chick[1]
                if (abs(er-r) + abs(ec-c)) < tmp:
                    tmp = abs(er-r) + abs(ec-c)
            cnt += tmp
            if tmp > rst:
                return
        rst = min(rst, cnt)
        return

    # 예를 들어, 첫 번째 인덱스라면, 0, 1의 치킨집을 골라 거리를 계산하고 return되어 와서 0, 2인덱스의 치킨집을 고른다.(백트래킹)
    for i in range(index, chicks_len):
        ans.append(chicks[i])
        solve(m+1, i+1)
        ans.pop()


N, M = map(int, sys.stdin.readline().strip().split())

city = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

# 1이면 homes에, 2면 chicks에 더해준다.
homes = []
chicks = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append((i, j))
        elif city[i][j] == 2:
            chicks.append((i, j))

# dfs 탐색을 위해 길이를 구해준다.
chicks_len = len(chicks)

# ans는 임시로 사용할 치킨집의 위치를 저장하는 배열
ans = []
rst = 9e9

# 완전탐색을 위해 첫 인덱스 부터 쭉 돌려준다. (-M+1)은 그 이상 가봐야 의미없다.
for i in range(chicks_len-M+1):
    solve(0, i)

print(rst)