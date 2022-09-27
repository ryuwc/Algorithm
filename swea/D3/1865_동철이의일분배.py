import sys; sys.stdin = open('1865.txt')
# import sys; sys.stdin = open('ssssss.txt', 'r')

# sums는 지금까지의 확률 더한거
def solve(index, sums):
    global rst
    # rst 갱신점
    if index == N:
        rst = max(rst, sums)
        return
    # 간단한 가지치기
    if sums <= rst:
        return
    # 이 역시 같은 행과 열을 가질 수 없음
    for j in range(N):
        if visit[j]:
            continue
        if info[index][j] == 0:
            continue
        visit[j] = 1
        solve(index+1, sums*(info[index][j]/100))
        visit[j] = 0

for tc in range(int(input())):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]

    visit = [0]*N
    rst = -1
    solve(0, 100)

    # 출력 방식대로 바꾸는 방법
    # 1. round함수를 사용해 소숫자리 7번째에서 반올림 해준다.
    # 2. format함수를 사용해 나머지 부분을 0으로 채워준다.
    print(f'#{tc+1}', '{:.6f}'.format(round(rst, 6)))
