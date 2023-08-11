def main():
    T = int(input())
    for tc in range(T):
        N, stst = map(str, input().split())
        N = int(N)

        for st in stst:
            print(st*N, end='')
        print()

main()