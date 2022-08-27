# import sys; sys.stdin = open("4864.txt", "r")
#
#
# for tc in range(int(input())):
#     str1 = input()
#     str2 = input()
#     N = len(str1)
#     M = len(str2)
#     result = 0
#     for i in range(M-N+1):
#         if str2[i:N+i] == str1:
#             result += 1
#     print(f'#{tc+1} {result}')

#==================================
# 슬라이싱 사용 x
import sys; sys.stdin = open("4864.txt", "r")

for tc in range(int(input())):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)
    result = 0

    i = j = 0
    while i < M and j < N:
        if str2[i] != str1[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == N:
        result += 1

    print(f'#{tc+1} {result}')