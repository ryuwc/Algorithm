import sys

def main():
    rst = 0
    for _ in range(N):
        st = sys.stdin.readline().strip()
        if len(st) % 2 == 1:
            continue
        stack = []
        stack.append(st[0])
        for i in range(1, len(st)):
            if stack and st[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(st[i])

        if not stack:
            rst += 1

    return rst


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())

    print(main())

