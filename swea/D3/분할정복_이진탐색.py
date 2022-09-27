import sys; sys.stdin = open('input_이진탐색.txt', 'r')

def quick_sort(low, high):
    if low >= high: return
    i = low-1
    for j in range(low, high):
        if A[j] <= A[high]:
            i += 1
            A[j], A[high] = A[high], A[j]
    i += 1
    A[i], A[high] = A[high], A[i]

    quick_sort(low, i-1)
    quick_sort(i+1, high)

def binary_search(low, high, target):
    global flag_l, flag_r, rst
    if low > high: return
    mid = (low + high) // 2
    if A[mid] == target:
        rst += 1
        return 1
    elif A[mid] > target:
        if flag_l:
            flag_l = False
            flag_r = True
            if binary_search(low, mid-1, target):
                return 0
        else:
            return 0
    else:
        if flag_r:
            flag_r = False
            flag_l = True
            if binary_search(mid+1, high, target):
                return 0
        else:
            return 0
        return 0

for tc in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))


    rst = 0
    for val in B:
        flag_l = True
        flag_r = True
        binary_search(0, N-1, val)
    print(f'#{tc+1} {rst}')

