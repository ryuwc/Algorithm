import sys;
sys.stdin = open('input_노드의 합.txt', 'r')
sys.setrecursionlimit(10 ** 6)

def postorder(v, tree, N):
    if v > N:
        return 0
    else:
        left = postorder(2*v, tree, N)
        right = postorder(2*v + 1, tree, N)
        tree[v] += left + right
        return tree[v]

def main():
    T = int(input())
    for tc in range(1, T+1):
        N, M, L = map(int, input().split())
        tree = [0] * (N+1)
        for _ in range(M):
            idx, val = map(int, input().split())
            tree[idx] = val

        postorder(1, tree, N)
        print(f'#{tc} {tree[L]}')

if __name__ == '__main__':
    main()
