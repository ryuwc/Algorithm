import sys; sys.stdin = open('input_2817.txt', 'r')

def solve(s):
    global result
    # if s == 3:
    #     print(ans)
    #     return
    if s == K:
        result += 1
        # print(ans)
        return
    elif s > K:
        return
    for i in range(N):
        if visited[i]:
            continue
        if not ans or ans[-1] > i:
            visited[i] = 1
            ans.append(i)
            solve(s+nums[i])
            ans.pop()
            visited[i] = 0

for tc in range(int(input())):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    visited = [0]*(N+1)
    result = 0
    ans = []
    solve(0)
    print(f'#{tc+1}', result)