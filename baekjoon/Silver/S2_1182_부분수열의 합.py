
N, S = map(int, input().split())
arr = list(map(int, input().split()))

result = []
def dfs(index, path):
    global result
    result.append(path)

    for i in range(index, N):
        dfs(i+1, path+[arr[i]])

dfs(0, [])

ans = 0
for i in range(len(result)):
    if len(result[i])>0 and sum(result[i]) == S:
        ans += 1

print(ans)
