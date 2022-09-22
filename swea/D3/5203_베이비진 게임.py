import sys; sys.stdin = open('sample_input_베이비진.txt', 'r')
# import sys; sys.stdin = open('sample_input_베이비진 - 복사본.txt', 'r')

def check(p):
    global flag, A, B
    if p == 1:
        A.sort()
        for i in range(10):
            if A.count(i) >= 3:
                flag[0] = True
                return 1
        for i in range(len(A)-2):
            if (A[i]+1) in A and (A[i]+2) in A:
                flag[0] = True
                return 1
    elif p == 2:
        B.sort()
        for i in range(10):
            if B.count(i) >= 3:
                flag[1] = True
                return 1
        for i in range(len(B) - 2):
            if (B[i]+1) in B and (B[i]+2) in B:
                flag[1] = True
                return 1

for tc in range(int(input())):
    info = list(map(int, input().split()))
    A = []
    B = []
    flag = [False, False]
    for _ in range(0, len(info), 2):
        a, b = info[_], info[_+1]
        A.append(a)
        if check(1):
            break
        B.append(b)
        if check(2):
            break

    if flag[0] and not flag[1]:
        print(f'#{tc+1}', 1)
    elif flag[1] and not flag[0]:
        print(f'#{tc+1}', 2)
    else:
        print(f'#{tc+1}', 0)
