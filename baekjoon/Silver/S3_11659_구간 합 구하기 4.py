import sys; from math import ceil, log

def init(node, start, end):
    # 리프 노드임
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    else:
        # bottom -> top 방식으로 내려가면서 값을 구하고 그 값을 올려줘서 더해줌
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
        return tree[node]

def sub_sum(node, start, end, left, right):
    # 탐색 구간이 벗어난 경우는 0을 return
    if left > end or right < start:
        return 0

    # 쪼개고 쪼개서 완전히 포함되는 경우 -> 더 쪼개서 봐야됨 -> 그러다 0이 나오거나 여기서 return 한번 더 되면 그 값을 리턴하면 됨
    # 재귀적인 부분이라 설명이 어렵네요
    if left <= start and end <= right:
        # print(tree[node])
        return tree[node]

    return sub_sum(node*2, start, (start+end)//2, left, right) + sub_sum(node*2 + 1, (start+end)//2+1, end, left, right)

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    nums = list(map(int, sys.stdin.readline().strip().split()))

    tree = [0] * 2**(ceil(log(N, 2) + 1))
    init(1, 0, N-1)
    # print(tree)
    for _ in range(M):
        left, right = map(int, sys.stdin.readline().strip().split())
        print(sub_sum(1, 0, N-1, left-1, right-1))
        # sub_sum(1, 0, N - 1, left - 1, right - 1)
        # print('---------------------')
