
N, S = map(int, input().split())
arr = list(map(int, input().split()))

result = []
# dfs를 사용하여 모든 부분 수열을 만들어서 result에 저장
def dfs(index, path):
    global result
    result.append(path)

    for i in range(index, N):
        dfs(i+1, path+[arr[i]])

dfs(0, [])

ans = 0
for i in range(len(result)):
    # 부분 수열이 []으로 빈 리스트도 포함되어서 sum([])은 0이 되어버림 그래서 조건 추가
    if len(result[i])>0 and sum(result[i]) == S:
        ans += 1

print(ans)
