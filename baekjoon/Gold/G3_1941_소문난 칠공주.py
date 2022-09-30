import sys
# sys.stdin = open('칠공주.txt', 'r')
sys.setrecursionlimit(10**6)

# dfs와 bfs가 섞여서 사용됨
def solve(nums, S, Y):
    global rst, visit
    if Y > 3: return
    # 중복 방지를 위해 7개의 글자의 좌표를 정렬해서 튜플로 묶어서 visit이란 set에 저장
    if len(nums) == 7:
        nums = tuple(sorted(nums))
        if nums not in visit:
            rst += 1
            visit.add(nums)
            return
        return
    # 여기서 부터가 bfs섞인 부분, nums에 넣어준 좌표들을 pop하면 안됨 그냥 읽으면 됨
    for num in nums:
        r, c = num[0], num[1]
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                # 방문 여부를 확인하기 위한 작업, 그냥 nums안에 있으면 방문했던 곳임
                if (nr, nc) not in nums:
                    if students[nr][nc] == 'Y':
                        solve(nums+[(nr, nc)], S, Y+1)
                    else:
                        solve(nums+[(nr, nc)], S+1, Y)

students = [list(map(str, input())) for _ in range(5)]
N = 5

visit = set()

rst = 0
for i in range(N):
    for j in range(N):
        if students[i][j] == 'S':
            solve([(i, j)], 1, 0)
        else:
            solve([(i, j)], 0, 1)
print(rst)