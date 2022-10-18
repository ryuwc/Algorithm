import sys

def solve(index, cal):
    global min_num, max_num
    if index == N:
        min_num = min(min_num, cal)
        max_num = max(max_num, cal)
        return

    val = nums[index]

    candi = [cal+val, cal-val, cal*val, int(cal/val)]

    if oper[0] > 0:
        oper[0] -= 1
        solve(index+1, candi[0])
        oper[0] += 1

    if oper[1] > 0:
        oper[1] -= 1
        solve(index+1, candi[1])
        oper[1] += 1

    if oper[2] > 0:
        oper[2] -= 1
        solve(index+1, candi[2])
        oper[2] += 1

    if oper[3] > 0:
        oper[3] -= 1

        solve(index+1, candi[3])
        oper[3] += 1

N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
oper = list(map(int, sys.stdin.readline().strip().split()))

min_num = 9e9
max_num = -9e9

solve(1, nums[0])

print(max_num)
print(min_num)