### 풀이

```python
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
```

---

### comment

- N과 M문제를 응용해서 풀 수 있는 탐색, 백트래킹 문제였다.
- 이 문제에서는 depth를 선수의 포지션이 하나씩 정해주는 것을 뜻한다.
- 즉, depth를 열번호로 사용한다. 하나의 열에 요소가 있으면, 다른 요소를 사용해야 한다.
- 첫번째 행에서 요소를 정하고, 다음 행에서 요소를 정할 때 그 요소가 있는 열은 사용하지 못한다.
- 트리로 그려본다면 밑 그림과 같다.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb3Yn1a%2FbtrMDXvzliG%2F4jDBO1ZKOgP1IYQOXOmKkK%2Fimg.jpg" title="" alt="image" width="372">

- 그림에서 첫 번째 행에서 1을 정해주고 두번째 행에서 사용 가능한 요소는 6, 7, 8이다.
- 이런식으로 밑으로 내려가고, 밑에 더이상 값이 없으면(depth==M)이 되면, return한다.
- 1, 6, 11, 1, 6, 12, 1, 7, 10, 1, 7, 12, 1, 8, 10, 1, 8, 11 순서로 탐색할 것이다.
- 1에서 8이 return해 오면 더이상 들어갈 곳이 없으니 첫 번째 행은 다음 요소 2를 잡고 같은 과정을 반복한다.
