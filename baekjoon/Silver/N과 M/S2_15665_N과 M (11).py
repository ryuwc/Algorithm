import sys

def solve(depth, N, M):
    if depth==M:
        print(*ans)
        return
    # 현재 저장하고 있는 값을 표현, 중복 제거
    tmp = 0
    # 이 문제는 인덱스를 for문에 사용해야 한다.
    for i in range(len(arr)):
        # 방문했거나, tmp가 현재의 값과 같으면 continue
        if tmp == arr[i]:
            continue
        # visited[i] = 1
        ans.append(arr[i])
        tmp = arr[i]
        solve(depth + 1, N, M)
        val = ans.pop()
        # visited[i] = 0


N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
# 인덱스를 visited에 사용할 것이므로 N만큼 visited를 설정
visited = [0] * N
ans = []
solve(0, N, M)
