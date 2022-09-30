import sys; sys.stdin = open('5249.txt', 'r')


def find_set(x):
    while x != p[x]:  # 루트인지 아닌지
        x = p[x]
    return x

for tc in range(int(input())):
    N, E = map(int, input().split())

    # 간선들의 리스트 저장 [[u, v, weight], ...]
    edges = [list(map(int, input().split())) for _ in range(E)]

    # kruskal 알고리즘
    # 1. 간선들의 가중치를 오름차순으로 정렬
    # 근데, 이번에는 pop을 사용할것 내림차순으로 정렬
    edges.sort(key=lambda x:x[2], reverse=True)

    # disjoint-set 준비
    p = [i for i in range(N+1)]    # 0번 ~ N번의 정점 make-set()

    mst = []    # MST 간선들을 저장
    ans = 0     # 간선들의 가중치 합

    # 2. 가중치가 최소인 간선을 정점수 - 1개 선택
    cnt = N     # 정점수 = N + 1개이므로 MST의 간선수는 N개
    while cnt:
        u, v, weight = edges.pop()
        a = find_set(u)
        b = find_set(v)
        if a == b:      # 싸이클이 생기는 간선이므로 pass
            continue    # cnt가 줄지 않음
        ans += weight
        mst.append([u, v, weight])

        p[a] = b        # union-set(a, b) 또는 p[b] = a
        cnt -= 1

    print(f'#{tc+1}', ans)
