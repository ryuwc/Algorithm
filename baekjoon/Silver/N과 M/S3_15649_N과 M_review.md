# N과 M (1)

---

### 코드

```python
import sys

def solve(depth, N, M):
    # depth가 M과 같아질 때 리턴
    if depth == M:
        print(*ans)
        return
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = 1
        ans.append(i)
        solve(depth+1, N, M)
        # 리턴 후 실행될 코드
        # for문이 끝나도 실행이 된다.
        ans.pop()
        visited[i] = 0



N, M = map(int, sys.stdin.readline().split())
arr = []
for i in range(1, N+1):
    arr.append(i)

visited = [0] * (N+1)
ans = []
solve(0, N, M)
```

### 

### 재귀 , 백트래킹

- ans에는 stack처럼 for문을 사용해 값을 넣어준다.

- 넣어주고, 재귀를 돌린다.

- depth가 m과 같아질 때 리턴을 건다.

- 리턴이 되면, pop()이 실행되어 ans의 맨 뒤의 요소가 빠진다.

- 또한, for문이 끝나도, pop()이 실행된다. 이때, i는 맨 처음 넣어논 1이 된다.

- 그 다음은 2가 쌓일 것이다.

- for문안에 for문이 돌아가는 구조로 복잡하다.

---

### 

### 트리로 표현

- 재귀를 구현하기 전 트리의 형태로 작성하여 코드를 짜본다.

- 이 경우, N이 3이고, M도 3일 때, 아래 그림과 같이 순회한다.

![이미지](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcJmTRj%2FbtrMd2K609V%2F8PKdv8gk1NITGv2dbcul00%2Fimg.jpg)

- 리턴(pop)이 돌며, 다음 숫자로 계속 순회한다.

---

# 

# N과 M (2)

---

### 코드

```python
import sys

def solve(depth, N, M):
    # depth가 M과 같아질 때 리턴
    if depth == M:
        print(*ans)
        return
    for i in range(1, N+1):
        if visited[i]:
            continue
        if not ans:
            visited[i] = 1
            ans.append(i)
            solve(depth + 1, N, M)
            ans.pop()
            visited[i] = 0
        elif i > ans[-1]:
            visited[i] = 1
            ans.append(i)
            solve(depth+1, N, M)
            ans.pop()
            visited[i] = 0




N, M = map(int, sys.stdin.readline().split())
arr = []
for i in range(1, N+1):
    arr.append(i)

visited = [0] * (N+1)
ans = []
solve(0, N, M)
```

### 구현 아이디어

- (1)의 코드에서 살짝 수정해주면 된다.

- 함수의 실행 부분을 조건을 걸어서 둘로 나눠준다.
  
  - ans가 비었다면 함수 실행 및 재귀
  
  - ans의 마지막 인덱스 요소가 자기보다 크다면 함수 실행 및 재귀

- 잘 작동한다.



---

# N과 M (3)

---



### 코드

```python
import sys

def solve(depth, N, M):
    # depth가 M과 같아질 때 리턴
    if depth == M:
        print(*ans)
        return
    for i in range(1, N+1):
        # if visited[i]:
        #     continue
        # visited[i] = 1
        ans.append(i)
        solve(depth+1, N, M)
        # 리턴 후 실행될 코드
        # for문이 끝나도 실행이 된다.
        ans.pop()
        visited[i] = 0



N, M = map(int, sys.stdin.readline().split())
arr = []
for i in range(1, N+1):
    arr.append(i)

visited = [0] * (N+1)
ans = []
solve(0, N, M)

```

---



### comment

- N과 M (1) 이 중복 없이 수열을 출력하는 것이면, 이번 문제는 중복이 가능하다.

- 따라서, visited라는 조건문을 없애주면 쉽게 풀 수 있다.



---

N과 M (4)

---



### 코드

```python
import sys

def solve(depth, N, M):
    # depth가 M과 같아질 때 리턴
    if depth == M:
        print(*ans)
        return
    for i in range(1, N+1):
        # if visited[i]:
        #     continue
        if not ans:
            # visited[i] = 1
            ans.append(i)
            solve(depth + 1, N, M)
            ans.pop()
            visited[i] = 0
        elif i >= ans[-1]:
            # visited[i] = 1
            ans.append(i)
            solve(depth+1, N, M)
            ans.pop()
            visited[i] = 0




N, M = map(int, sys.stdin.readline().split())
arr = []
for i in range(1, N+1):
    arr.append(i)

visited = [0] * (N+1)
ans = []
solve(0, N, M)

```

---



### comment

- N과 M (2)번 문제를 조금만 수정하면 된다.

- 일단, 중복이 가능하니 visited를 빼준다.

- 그 후, 2 번의 경우에는 다음에 넣어줄 숫자가 자신보다 크면이었지만, 이 조건을

- 자신보다 크거나 같으면 으로 바꿔주면 된다.



---

# N과 M (5)

---



### 코드

```python
import sys

def solve(depth, N, M):
    if depth == M:
        print(*ans)
        return
    for i in arr:
        if visited[i]:
            continue
        visited[i] = 1
        ans.append(i)
        solve(depth+1, N, M)
        # return후 할 작업
        ans.pop()
        visited[i] = 0



N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
max_arr = max(arr)
visited = [0] * (max_arr+1)
ans = []

solve(0, N, M)
```

---



### comment

- N과 M 1번 문제를 조금 수정하면 된다.

- for문이 도는걸 list로 받은 arr로 돌게 해주면 된다.



---

# N과 M (6)

---

### 코드

```python
import sys

def solve(depth, N, M):
    if depth == M:
        print(*ans)
        return
    for i in arr:
        if visited[i]:
            continue
        if not ans:
            visited[i] = 1
            ans.append(i)
            solve(depth+1, N, M)
            ans.pop()
            visited[i] = 0
        elif i > ans[-1]:
            visited[i] = 1
            ans.append(i)
            solve(depth+1, N, M)
            ans.pop()
            visited[i] = 0



N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
max_arr = max(arr)
visited = [0] * (max_arr+1)
ans = []

solve(0, N, M)
```

---

### comment

- N과 M (2)에서 약간 수정해주면 된다.

- for문을 arr로 순회하게 해주면 된다.



---

# N과 M (7)

---

### 코드

```python
import sys

def solve(depth, N, M):
    if depth==M:
        print(*ans)
        return
    for i in arr:
        ans.append(i)
        solve(depth+1, N, M)
        ans.pop()





N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
max_arr = max(arr)
visited = [0] * (max_arr+1)
ans = []

solve(0, N, M)
```

---



### comment

- 그냥 visited없애주고 arr에서 for문이 돌게 하면 된다.
