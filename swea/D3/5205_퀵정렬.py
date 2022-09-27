import sys; sys.stdin = open('5205.퀵정렬.txt', 'r')

def quick_sort(low, high):
    if low >= high: return

    i = low-1
    for j in range(low, high):
        if nums[j] <= nums[high]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    i += 1
    nums[i], nums[high] = nums[high], nums[i]
    quick_sort(low, i-1)
    quick_sort(i+1, high)

for tc in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    A = [0]*N
    quick_sort(0, N-1)
    print(f'#{tc+1}', nums[N//2])