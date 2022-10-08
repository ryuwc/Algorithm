import sys
sys.setrecursionlimit(10**6)

# index = 현재 일정, profit = 현재까지의 수익
def solve(index, profit):
    global rst
    # index가 초과하면 rst를 갱신
    if index >= N:
        rst = max(rst, profit)
        return
    # 상담 소요일
    now_num = meeting[index][0]
    # 상담 수익
    now_profit = meeting[index][1]
    # 현재 상담을 안하고 다음날로 넘어가기
    solve(index+1, profit)

    # index에러 방지 == 상담 할 수 있는 경우
    if now_num + index <= N:
        # 상담 진행
        solve(index+now_num, profit+now_profit)

N = int(sys.stdin.readline().strip())

meeting = []
for _ in range(N):
    val = list(map(int, sys.stdin.readline().strip().split()))
    meeting.append(val)

rst = -1
for i in range(N):
    solve(i, 0)

print(rst)


