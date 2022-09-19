# import sys
#
#
# # N과 M을 풀었다면 똑같이 풀면 됨
#
# def solve(depth, K):
#     if depth == 6:
#         print(*ans)
#         return
#     for i in S:
#         if visited[i]:
#             continue
#         if not ans:
#             ans.append(i)
#             visited[i] = 1
#             solve(depth + 1, K)
#
#             ans.pop()
#             visited[i] = 0
#         elif i > ans[-1]:
#             ans.append(i)
#             visited[i] = 1
#             solve(depth+1, K)
#
#             ans.pop()
#             visited[i] = 0
#
# while 1:
#     K, *S = map(int, sys.stdin.readline().split())
#     if K == 0:
#         break
#     visited = [0] * 50
#     ans = []
#
#     solve(0, K)
#     print()

#=========================================================================
import sys
from itertools import combinations
while 1:
    K, *S = map(int, sys.stdin.readline().split())
    if K == 0:
        break
    ans = combinations(S, 6)
    for line in ans:
        print(*line)
    print()