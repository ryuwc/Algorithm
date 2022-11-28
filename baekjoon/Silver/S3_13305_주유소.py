import sys

N = int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().strip().split()))
citys = list(map(int, sys.stdin.readline().strip().split()))

# 첫 번째 도시에서는 무조건 다음 도시로 이동할 거리만큼 기름을 채워야 한다.
rst = dist[0] * citys[0]
# 현재 기름 가격은 0번째 city
now_price = citys[0]
# 현재 위치 == 거리
now = 0

for i in range(1, N-1):
    now = dist[i]
    # 다음 도시의 가격이 현재 가격보다 낮으면 그 가격으로 기름을 채움
    if citys[i] < now_price:
        now_price = citys[i]
        rst += now * now_price
    # 아니라면 다녀온 도시 중 가장 싼 곳의 가격으로 기름을 구매
    else:
        rst += now_price * now

print(rst)
