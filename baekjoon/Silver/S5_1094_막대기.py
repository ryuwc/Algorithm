N = int(input())

# 일단 64길이의 막대가 있으니, 잘라서 만들 수 있는 막대기의 길이를 다 넣어줬다.
stick = [64, 32, 32, 16, 16, 8, 8, 4, 4, 2, 2, 1, 1]

for i in range(1<<len(stick)):  # 비트 연산자를 활용해 경우의 수를 확인해본다.
    sums = 0; count = 0         # sums는 n개의 막대가 나올 때 길이의 합, count는 갯수
    for j in range(len(stick)):
        if i & (1<<j):
            sums += stick[j]    # 더해주고 카운트해준다.
            count += 1
    if sums == N:               # sums이 N과 같아진다면, 그 갯수를 출력한다.
        print(count)
        break