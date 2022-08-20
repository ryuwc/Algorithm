import sys; sys.stdin = open('input_숫자회전.txt', 'r')

for tc in range(int(input())):
    N = int(input())
    arr = []
    for _ in range(N):
        arr += [list(map(int, input().split()))]

    ans1 = [['']*N for _ in range(N)]       # 숫자들을 문자열로 만들 빈 리스트 생성 -> [['', '', ''], ['', '', ''], ['', '', '']]
    print(ans1)
    for j in range(N):
        for i in range(N-1, -1, -1):   
            ans1[j][0] += str(arr[i][j])    # 90도 돌려준것을 문자열로 빈 리스트 인덱스 0리스트에 삽입

    for i in range(N-1, -1, -1):            # 180도 돌려주는데, 위와 아래가 바뀌어 있어서, 밑의 과정으로 재 정렬해줌
        for j in range(N-1, -1, -1):
            ans1[i][1] += str(arr[i][j])
    for i in range(N//2):
        ans1[N-i-1][1], ans1[i][1] =ans1[i][1], ans1[N-i-1][1]   # N//2번 정렬하고 위와 아래를 바꿔준다 밑에도 같음

    for j in range(N-1, -1, -1):
        for i in range(N):
            ans1[j][2] += str(arr[i][j])

    for i in range(N//2):
        ans1[N-i-1][2], ans1[i][2] = ans1[i][2], ans1[N-i-1][2]

    print(f'#{tc+1}')
    for line in ans1:
        print(*line)

