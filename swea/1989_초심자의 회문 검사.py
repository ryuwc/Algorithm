T = int(input())

for tc in range(1, T+1):
    text = input()
    N = len(text)
    arr = list(text)
    for i in range(N//2):
        arr[i], arr[N-1-i] = arr[N-1-i], arr[i]
    rev_text = ''.join(arr)
    if arr == list(text):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')