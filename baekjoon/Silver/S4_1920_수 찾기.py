import sys;

def solve(start, end, num):
    if start >= end:
        print(0)
        return
    mid = (start+end) // 2
    if arr1[mid] == num:
        print(1)
        return

    if arr1[mid] < num:
        solve(mid+1, end, num)
    else:
        solve(start, mid, num)


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    arr1 = list(map(int, sys.stdin.readline().strip().split()))

    M = int(sys.stdin.readline().strip())
    arr2 = list(map(int, sys.stdin.readline().strip().split()))

    arr1.sort()

    for num in arr2:
        solve(0, N, num)


