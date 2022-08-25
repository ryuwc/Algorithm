import sys; sys.stdin = open('input_퍼펙트셔플.txt', 'r')

for tc in range(int(input())):
    N = int(input())
    half = N//2
    cards = list(input().split())
    card1 = []
    card2 = []
    result = []
    if N % 2 == 0:
        card1 = cards[:half]
        card2 = cards[half:]
        for i in range(half):
            result.append(card1[i])
            result.append(card2[i])
    else:
        card1 = cards[:half+1]
        card2 = cards[half+1:]
        for i in range(half):
            result.append(card1[i])
            result.append(card2[i])
        result.append(card1[-1])
    print(f'#{tc+1}', *result)