import sys; sys.stdin = open('1952.txt')

def solve(index, cost):
    global rst
    if cost > rst: return
    if index >= 12:
        rst = min(cost, rst)
        return
    if schedule[index]:
        solve(index+1, cost+(schedule[index] * d))
        solve(index+1, cost+m)
        solve(index+3, cost+m3)
        solve(index+12, cost+y)
    else:
        solve(index+1, cost)

for tc in range(int(input())):
    d, m, m3, y = map(int, input().split())
    schedule = list(map(int, input().split()))

    rst = 0xffffffff
    solve(0, 0)
    print(f'#{tc+1}', rst)
