nums = list(map(int, input().split()))
N = len(nums)
arr = [0]*N
c = [0] * (max(nums) + 1)

for num in nums:
    c[num] += 1
for i in range(1, len(c)):
    c[i] += c[i-1]
for i in range(len(arr)-1, -1, -1):
    c[nums[i]] -= 1
    arr[c[nums[i]]] = nums[i]

print(*arr)