import sys

def solve():
    # 임시로 넣어줄 숫자들 (여기서 pop할 거임)
    nums = []
    # +, -를 넣어줄 결과 (리턴할 거임)
    rst = []
    # 확인해야할 인덱스를 나타냄
    now = 0
    for i in range(1, N+1):
        nums.append(i)
        rst.append('+')
        while True:
            if not nums: break
            if nums[-1] == target[now]:
                nums.pop()
                now += 1
                rst.append('-')
            elif now >= N:
                break
            else:
                break
    # now가 N이 아니면 수열을 만들지 못하는 상황임
    if now != N:
        return 'NO'
    return rst

N = int(sys.stdin.readline())

target = []
for tc in range(N):
    num = int(sys.stdin.readline())
    target.append(num)

rst = solve()
if rst == 'NO':
    print('NO')
else:
    for r in rst:
        print(r)
