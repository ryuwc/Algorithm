## 풀이

```python
import sys;
from collections import deque

def bfs(N, M, r, c):
    Q.append((r, c))
    visited = [[0] * M for _ in range(N)]  # 이 문제의 경우, visited를 bfs 함수 안에 넣어줘야한다.
    visited[r][c] = 1
    sums = 0
    while Q:
        r, c = Q.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr, nc = r + di, c + dj
            if 0 <= nr < N and 0 <= nc < M:
                if maps[nr][nc] == 'L' and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1
                    sums = max(sums, visited[nr][nc])
                    Q.append((nr, nc))
    return sums - 1

N, M = map(int, sys.stdin.readline().split())

maps = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

Q = deque()
visited = [[0] * M for _ in range(N)]

result = 0
for i in range(N):
    for j in range(M):
        '''
        그냥 map이 L일 때 bfs를 돌리면, 모든 L에 대해 bfs를 돌리기 때문에
        시간 초과가 난다.
        간단한 조건만 걸어주면 된다.
        조건은 map이 L이고 양 옆, 또는 위 아래가 L이 아닐 때 bfs를 돌리면 된다.
        최적의 조건은 아닌 것 같지만 어찌저지 통과는 된다.
        '''
        if maps[i][j] == 'L' and visited[i][j] == 0:
            if 0 <= i - 1 < N and 0 <= i + 1 < N:
                if maps[i - 1][j] == 'L' and maps[i + 1][j] == 'L':
                    continue
            if 0 <= j - 1 < M and 0 <= j + 1 < M:
                if maps[i][j - 1] == 'L' and maps[i][j + 1] == 'L':
                    continue
            result = max(result, bfs(N, M, i, j))

print(result)
```

---

## COMMENT

여기에 bfs가 돌아가지 않게 조건을 하나 걸어주면 된다. L이고 양옆이 L이면 그 지점에선 안돌아가도 된다.

위아래 도 똑같다.

주석에도 달아놨지만, 최적의 조건은 아닌것같지만 어찌저지 돌아간다.

일단, 지금까지 했던 bfs와는 조금 달랐다.

지금 까지 dfs, bfs탐색을 할 때는 visited를 함수 밖에 만들어 줬다.

처음에 함수 밖에 만들고, visited의 가장 큰 수를 출력하는 코드를 짰는데, 틀렸다.

이 문제의 경우, visited를 함수 안에 만들어 함수가 돌아갈때마다 visited를 초기화해야 했다.

그런데, 이경우 bfs를 돌릴때 조건을 if maps[i][j] == 'L'일 때, 돌아가게 했어야 했는데,

기존 사용하던 if maps[i][j] == 'L' and visited[i][j]를 사용할 수 없어

bfs는 L 일 때 모두 돌아가게 된다.

하지만, 이경우 **시간초과**가 난다.

여기에 bfs가 돌아가지 않게 조건을 하나 걸어주면 된다. L이고 양옆이 L이면 그 지점에선 안 돌아가도 된다.

위아래 도 똑같다.

주석에도 달아놨지만, 최적의 조건은 아닌것같지만 어찌 저찌 돌아간다.
