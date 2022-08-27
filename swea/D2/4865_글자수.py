import sys; sys.stdin = open("4865.txt", "r")

for tc in range(int(input())):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)
    result = [0]*N
    for i in range(N):
        for j in range(M):
            if str1[i] == str2[j]:
                result[i] += 1
    max_str = 0
    for i in range(N):
        if result[i] > max_str:
            max_str = result[i]
    print(f'#{tc+1} {max_str}')
