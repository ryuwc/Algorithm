import sys; sys.stdin = open('5247.txt', 'r')

from collections import deque

def solve(num):
    global rst
    # print(nums)
    Q = deque()
    Q.append((num, 0))
    visit.add(num)
    while Q:
        now, cnt = Q.popleft()
        if now == M:
            rst = min(rst, cnt)
            return
        tmp = [now+1, now-1, now*2, now-10]
        for val in tmp:
            if val not in visit and 0 < val <= 1000000:
                visit.add(val)
                Q.append((val, cnt+1))

for tc in range(int(input())):
    N, M = map(int, input().split())

    visit = set()
    rst = 987654321
    solve(N)
    print(f'#{tc+1}', rst)
