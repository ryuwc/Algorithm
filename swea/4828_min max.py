
T = int(input())

for _ in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    for i in range(N, 0, -1):
        for j in range(1, i):
            if nums[j - 1] > nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
    print(f'#{_} {nums[-1] - nums[0]}')


