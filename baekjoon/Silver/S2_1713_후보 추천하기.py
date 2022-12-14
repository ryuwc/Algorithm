import sys; from collections import deque
imput = sys.stdin.readline

N = int(input())
K = int(input())
students = list(map(int,input().split()))
max_student = max(students)
#
# result = [[0, 0, 0] for _ in range(max_student+1)]
#
# for i in range(max_student+1):
#     result[i][0] = i
#
# for i in range(K):
#     result[students[i]][1] += 1
#     result[students[i]][2] = i
#
# ans = sorted(result, key=lambda x:(-x[1], -x[2]))
#
# sol = []
# for i in range(N):
#     sol.append(ans[i][0])
#
# sol.sort()
# print(*sol)

# ===============================================================================================

result = {}
for i in range(K):
    key = students[i]
    if key in result.keys():
        result[key][0] += 1
    else:
        if len(result) < N:
            result[key] = [1, i]
        else:
            a = result.items()
            del_lst = sorted(result.items(), key=lambda x: (x[1][0], x[1][1]))
            del_key = del_lst[0][0]

            del result[del_key]

            result[key] = [1, i]

answer = list(sorted(result.keys()))
print(*answer)

#======================================================================
# n = int(input())
# num = int(input())
#
# def is_in_arr(arr , w):
#     for i in arr:
#         if i[2] == w:
#             return True
#     return False
#
# arr = []
# who = input().split()
# for idx, w in enumerate(who):
#     #1
#     if is_in_arr(arr, w):
#         #2
#         for index, var in enumerate(arr):
#             if var[2] == w:
#                 arr[index][0] += 1
#                 break
#     else:
#         #3
#         if len(arr) < n:
#             arr.append([1, idx, w])
#         else:
#             arr[0] = [1, idx, w]
#
#     arr.sort(key=lambda x: (x[0], x[1]))
#
# arr.sort(key=lambda x:int(x[2]))
# for i in range(n):
#     if i == n-1:
#         print(arr[i][2])
#     else:
#         print(arr[i][2], end = ' ')