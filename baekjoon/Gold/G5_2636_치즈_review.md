## 풀이

```python
import sys; from collections import deque

'''
이 문제의 핵심은 bfs를 통해 치즈를 녹이는 것이다.
외부인 공기에서 bfs를 시작하여 치즈를 녹이는 것이다.
'''
def bfs(N, M):
    Q.append((0, 0))
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    total = 0
    while Q:
        r, c = Q.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr, nc = r + di, c + dj
            if 0 <= nr < N and 0 <= nc < M:
                if cheese[nr][nc] == 0 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    Q.append((nr, nc))
                elif cheese[nr][nc] == 1:
                    cheese[nr][nc] = 0
                    total += 1
                    visited[nr][nc] = 1
    return total

N, M = map(int, sys.stdin.readline().split())
cheese = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
Q = deque()

cheese_lst = []     # 공기에 닿은 치즈의 갯수를 담을 리스트
cnt = 0             # 치즈가 모두 녹아 없어지는 시간
while True:
    cheese_lst.append(bfs(N, M))
    cnt += 1
    if sum(map(sum, cheese)) == 0:  # 남아있는 치즈가 없으면 break
        break

print(cnt)              # bfs가 돈 횟수 (치즈가 모두 녹아 없어지는 시간)
print(cheese_lst[-1])   # 마지막으로 bfs가 돈 횟수 (공기에 닿은 치즈의 갯수)
```

---

## COMMENT

- 풀고 나니까 간단한 로직인것 같다..
- 처음 접근할때, 치즈에 대해 탐색을 해야된다고 생각하여 dfs도 사용해보고 bfs도 사용해보고,
- 함수의 인자를 추가도 해봤지만, 답이 안보였다.
- 그러다, 문제 풀이의 핵심은 공기에서 탐색을 하여 치즈를 녹여야 한다는 것을 깨달았다.
- 공기에서 bfs가 한번 돌면, 치즈의 모퉁이는 사라지게 만든다.
- 치즈가 없어질 때 까지 bfs를 while문을 통해 반복한다.
- 이 과정에서 bfs가 돈 횟수, 마지막으로 남은 치즈의 갯수를 알아낼 수 있었다.
