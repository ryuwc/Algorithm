## 풀이

```python
import sys; from collections import deque

def bfs2():
    Q.append((0, 0, 0))
    visited[0][0][0] = 1
    while Q:
        r, c, z = Q.popleft()

        if r == N-1 and c == M-1:# 도착지점에 도달하면 returnreturn visited[r][c][z]

        for di, dj in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
            nr, nc = r + di, c + dj
            if 0 <= nr < N and 0 <= nc < M:
                if maze[nr][nc] == 0 and visited[nr][nc][z] == 0:# 벽이 아니고 방문하지 않았으면
                    visited[nr][nc][z] = visited[r][c][z] + 1
                    Q.append((nr, nc, z))
                elif maze[nr][nc] == 1 and z == 0:# 벽이고 벽을 부술 수 있으면
                    visited[nr][nc][z+1] = visited[r][c][z] + 1
                    Q.append((nr, nc, z+1))
    return -1
N, M = map(int, sys.stdin.readline().split())

maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

Q = deque()
'''
visited를 만들 때 3차원으로 만들어, 벽을 부순 횟수를 기록한다.
visited[r][c][z] = [0, 0]인데, z가 0이면 벽을 부수지 않은 상태, 1이면 벽을 부순 상태이다.
즉, visited[r][c][z]의 첫 번째 인덱스는 벽을 부수지 않은 상태에서의 최단 거리, 두 번째 인덱스는 벽을 부순 상태에서의 최단 거리이다.
'''
visited = [[[0] * 2 for _ in range(M)]for _ in range(N)]

print(bfs2())
```

---

## COMMENT

- 처음, 만약 움직이는 방향이 오른쪽이고, 벽이 있고, 길이 있으면 그 벽을 제거하고 끝내는 함수를 만들었다.
- 근데, 그렇게 짜면, 쓸데없이 벽을 부숴, 부셔야 되는 벽을 못 부수는 경우가 생긴다.
- 그렇다고 모든 경우의 수를 파악하고 코드를 짜자니, 이건 아닌 것 같다.
- 문제의 핵심은 visited를 3차원으로 만들어 벽을 깨지 않았을 때의 최단 거리, 벽을 깼을 때 최단 거리로 기록하여야 했다.
- 처음 접근을 어떻게 할 지 모르겠어서 다른 분들의 코드를 봤다.
- 이해하는데 많은 시간이 걸렸다.
- 만약 내 위치가 벽이고, 벽을 안 부순 상태라면 일단, 최단 거리를 visited[r][c][z] = [0, 0]의 1번 인덱스에 넣어주고,
- 위치와 벽을 부쉈다는 상태인 1을 Q에 넣어준다.
- 그리고 위의 Q의 차례가 오면 그 위치의 r, c는 z=1로 pop될 것이고, 이제는 벽을 부술 수 없다.
- 이 위치의 인접한 벽을 만나면 아무것도 못한다.
- 오직, 길인 0을 만났을 때, 최단 거리를 visited[r][c][z] = [0, 0]의 1번 인덱스에 넣어준다.
