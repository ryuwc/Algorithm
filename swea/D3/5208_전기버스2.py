import sys; sys.stdin = open('5208.txt')

def solve(index, cnt, gas):
    global rst
    gas -= 1
    if index >= (N-1):
        rst = min(rst, cnt)
        return
    if cnt >= rst: return

    #가스가 있는 경우
    if gas:
        solve(index+1, cnt, gas)
    # 가스가 없는 경우
    solve(index+1, cnt+1, info[index])

for tc in range(int(input())):
    N, *info = map(int, input().split())

    rst = 1e9

    # 이미 출발해서 0은 포함 안함
    solve(1, 0, info[0])

    print(f'#{tc+1}', rst)
