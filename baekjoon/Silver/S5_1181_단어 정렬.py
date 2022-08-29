import sys

N = int(sys.stdin.readline())
arr = set()
for i in range(N):                  # 중복된 원소가 들어가면 안되니까 set으로 넣어준다.
    arr.add(sys.stdin.readline().rstrip())
list(arr)
result = sorted(arr, key=lambda x:(len(x), x))   # 정렬에 lambda사용, 1순위는 길이, 2순위는 알파벳순...

for r in range(len(result)):
    sys.stdout.write(result[r])     # 처음 sys.stdout.write를 써봣다.
    sys.stdout.write('\n')          # 이거는 기본적으로 뒤에 개행문자가 안들어가 있는 것 같다.
