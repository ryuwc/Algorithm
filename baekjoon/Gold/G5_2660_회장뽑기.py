# import sys; from collections import deque, defaultdict
#
# def bfs(v):
#     visited = [0] * (N + 1)
#     Q.append((v, 0))
#     visited[v] = 1
#     max_visited = 0
#     while Q:
#         v, s = Q.popleft()
#         max_visited = max(max_visited, s)
#         for w in G[v]:
#             if not visited[w]:
#                 visited[w] = 1
#                 Q.append((w, s+1))
#     return max_visited
#
#
# N = int(sys.stdin.readline())
#
# G = [[] for _ in range(N+1)]
# while True:
#     u, v = map(int, sys.stdin.readline().split())
#     if u == -1 and v == -1:
#         break
#     G[u].append(v)
#     G[v].append(u)
# Q = deque()
#
#
# result = 0xfffff
# candidate = defaultdict(list)
# for i in range(1, N+1):
#     tmp = bfs(i)
#     result = min(result, tmp)
#     candidate[tmp].append(i)
#
#
# print(result, len(candidate[result]))
# for i in sorted(candidate[result]):
#     print(i, end=' ')

# ===================================================================
import sys; from collections import deque, defaultdict


def bfs(v):
    visited = [-1] * (N + 1)        # bfs함수 내에서 visited를 초기화
    visited[v] = 0                  # 시작점은 0으로 초기화
    Q.append(v)
    while Q:
        v = Q.popleft()
        for w in G[v]:
            if visited[w] == -1:
                visited[w] = visited[v] + 1
                Q.append(w)
    return max(visited)             # visited의 최대값이 점수이다.


N = int(sys.stdin.readline())

G = [[] for _ in range(N+1)]
while True:
    u, v = map(int, sys.stdin.readline().split())
    if u == -1 and v == -1:
        break
    G[u].append(v)
    G[v].append(u)
Q = deque()

result = 0xfffff
for i in range(1, N+1):
    tmp = bfs(i)
    if tmp < result:            # 회장이 될 수 있는 점수 찾기
        result = tmp

candidate = []
for i in range(1, N+1):
    if bfs(i) == result:
        candidate.append(i)     # 회장 후보들을 candidate에 저장

candidate.sort()
print(result, len(candidate))
print(*candidate)
