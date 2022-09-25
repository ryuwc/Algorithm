import collections; import sys
sys.setrecursionlimit(10**6)


for tc in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))

    graph = collections.defaultdict(list)

    # graph에 간선의 정보를 넣어줌
    for i in range(1, N+1):
        graph[i].append(nums[i-1])

    # traced 는 현재의 진행 상황, 간선을 타고 가다 traced안에 있으면 result를 1증가
    traced = set()
    # visit은 중복처리 방지용, 후위 순회로 정점을 순회한 뒤 return할 때 증가
    visited = set()


    result = 0
    def dfs(i):
        global result
        # traced안에 i가 있으면 순환구조그래프임
        if i in traced:
            result += 1
            return
        # 이미 방문 했던 적이 있는 정점이면 return (가지치기)
        if i in visited:
            return
        # 진행 상황을 넣어주고
        traced.add(i)
        # 다음 간선으로 타고감
        for x in graph[i]:
            dfs(x)
        traced.remove(i)
        visited.add(i)
    for i in range(1, N+1):
        dfs(i)
    print(result)