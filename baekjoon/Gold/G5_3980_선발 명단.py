def solve(depth):
    global result
    # depth를 포지션으로 정의 depth가 11이 되면, 포지션이 꽉 찬 상태
    if depth == 11:
        # 지금까지 넣어논 선수의 능력치를 모두 더한값을 정해주고 return
        result = max(result, sum(ans))
        return
    # 여기서 사용하는 i는 배열의 열, 행은 depth로 정의 즉, 배열의 열이 하나 있다면, 다른 행의 요소는 열 번호가 달라야함
    for i in range(11):
        if visited[i]:
            continue
        # 0이 아니라면
        if skill[depth][i]:
            visited[i] = 1
            ans.append(skill[depth][i])
            solve(depth+1)
            # 마지막 원소를 pop하며 다시 전으로 return됨
            ans.pop()
            visited[i] = 0

for tc in range(int(input())):
    skill = [list(map(int, input().split())) for _ in range(11)]

    result = 0
    ans = []
    # visited는 선수가 포지션에 있는지 확인 여부 (배열의 열을 쓰고 있는지)
    visited = [0]*12
    solve(0)
    print(result)
