from collections import deque
import sys

def bfs(v):                 # bfs 반복 코드
    Q.append(v)             # 일단, 시작점을 Q에 넣어준다.
    D[v] = 0                # D는 시작점 부터의 거리
    visited[v] = 1          # visited 방문 해주고
    while Q:                # Q가 빈 리스트가 될 때 까지
        v = Q.popleft()     # Q의 제일 앞인덱스를 뽑아준다.
        for w in G[v]:      # 노드가 갈 수 있는 곳
            if not visited[w]:  # 방문하지 않았다면
                Q.append(w)     # 그 노드를 Q에 append
                visited[w] = 1  # visited 방문하고
                D[w] = D[v] + 1 # 시작점 부터의 거리니까 D[v]에 +1
                P[w] = v        # 부모 저장


V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
G = [[] for _ in range(V+1)]

for _ in range(E):
    u, v = map(int, sys.stdin.readline().split())
    G[u].append(v)
    G[v].append(u)

Q = deque()
visited = [0]*(V+1)
D = [0] * (V+1)         # 시작점에서 최단 거리
P = [0] * (V+1)         # 최단 경로 트리 (부모 저장)

bfs(1)
result = 0
for i in range(len(visited)):
    if visited[i]:
        result += 1

print(result-1)






