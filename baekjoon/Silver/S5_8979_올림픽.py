# import sys
# from collections import defaultdict
# N, K = map(int, sys.stdin.readline().split())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#
# result1 = sorted(arr, key=lambda x:(x[1], x[2], x[3]), reverse=True)
#
# result2 = defaultdict(list)
# for i in range(1, 1001):
#     result2[i] = []
#
# cnt = 1
# for i in range(N):
#     val = result1[i][0]
#     score = result1[i][1:4]
#     if i == 0:
#         result2[cnt].append(val)
#     elif score == result1[i-1][1:4]:
#         result2[i].append(val)
#     else:
#         result2[cnt].append(val)
#     cnt += 1
# # print(result2)
#
# for key, value in result2.items():
#     if K in value:
#         print(key)

#+=============================================================================

import sys
N, K = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result1 = sorted(arr, key=lambda x:(x[1], x[2], x[3]), reverse=True)

for i in range(N):
    if result1[i][0] == K:
        index = i
for i in range(N):
    val1 = result1[index][1:]
    val2 = result1[i][1:]
    if val1 == val2:
        print(i+1)
        break
