import sys; sys.stdin = open('input_이진탐색.txt', 'r')

cnt = 1
def make_tree(v):
    global cnt
    if v > N:
        return
    # 왼쪽 자식의 인덱스는 현재 인덱스의 2배
    make_tree(v*2)
    # 현재 인덱스에 cnt를 저장
    tree[v] = cnt
    cnt += 1
    # 오른쪽 자식의 인덱스는 현재 인덱스의 2배 + 1
    make_tree(v*2+1)

for tc in range(int(input())):
    N = int(input())
    tree = [0] * (N+1)

    make_tree(1)
    print(f'#{tc+1} {tree[1]} {tree[N//2]}')
    cnt = 1


