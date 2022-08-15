N, M, K = map(int, input().split())

if M >= K:
    print((K)+(N-M))
elif M < K:
    print(M+(N-K))