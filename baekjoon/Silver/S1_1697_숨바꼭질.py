from collections import deque

def solve(num):
    global rst
    Q = deque()
    # Q에 현재 숫자와 움직임의 숫자를 넣어준다. 현재는 0
    Q.append((num, 0))
    # 중복 탐색 방지를 위해 visit에 현재 숫자 넣어준다
    visit.add(num)
    while Q:
        now, cnt = Q.popleft()
        # 답이 나온 경우
        if now == K:
            rst = min(cnt, rst)
            return
        # 움직일 수 있는 숫자
        can_move = [now+1, now-1, now*2]
        for val in can_move:
            # 중복 탐색 방지와 문제의 조건
            if val not in visit and 0 <= val <= 100000:
                Q.append((val, cnt+1))
                visit.add(val)

N, K = map(int, input().split())

rst = 1e9
visit = set()
solve(N)
print(rst)