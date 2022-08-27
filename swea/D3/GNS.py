
nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
for tc in range(1, T+1):
    TC, N = input().split()
    arr = input().split()
    idx = 0
    for i in range(len(nums)):
        for j in range(len(arr)):
            if arr[j] == nums[i]:
                arr[j], arr[idx] = arr[idx], arr[j]
                idx += 1

    print(f'#{tc}\n', *arr)


