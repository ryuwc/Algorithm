ahdma = 'aeiou'
def solve(depth):
    if depth == K:
        # 모음, 자음 숫자 확인
        a, b = 0, 0
        for _ in range(K):
            if ans[_] in ahdma:
                a += 1
            else:
                b += 1
        # 모음과 자음 개수가 안맞다면 return
        if not (a >=1 and b >= 2): return
        print(''.join(ans))
        return
    for i in range(N):
        if visited[i]: continue
        # ans에 값이 담겨 있고, ans의 마지막 원소의 아스키 코드값이 현재 넣을 요소의 아스키 코드 값보다 크면 다시 돌아가
        if len(ans) > 0:
            if ord(ans[-1]) > ord(code[i]): continue
        ans.append(code[i])
        visited[i] = True
        solve(depth+1)
        ans.pop()
        visited[i] = False

K, N = map(int, input().split())

code = list(map(str, input().split()))
code.sort()
visited = [False] * (N+1)
ans = []
solve(0)