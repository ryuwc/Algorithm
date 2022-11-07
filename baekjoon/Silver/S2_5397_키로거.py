import sys

for tc in range(int(sys.stdin.readline())):
    arr = list(sys.stdin.readline().strip())
    arr2 = []
    arr3 = []

    for word in arr:
        if word == '<' and arr2:
            arr3.append(arr2.pop())
        elif word == '>' and arr3:
            arr2.append(arr3.pop())
        elif word == '-' and arr2:
            arr2.pop()
        elif word.isalnum():
            arr2.append(word)
    arr3.reverse()
    rst = arr2 + arr3
    print(''.join(rst))
