N = int(input())
nums = list(map(int, input().split()))
target = int(input())

rst = 0
for num in nums:
    if num == target:
        rst += 1

print(rst)