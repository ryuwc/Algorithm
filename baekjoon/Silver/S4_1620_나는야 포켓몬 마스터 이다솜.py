import sys


def main():
    N, M = map(int, sys.stdin.readline().strip().split())
    pocket_dict1 = dict()
    pocket_dict2 = dict()

    for idx in range(1, N + 1):
        val = sys.stdin.readline().strip()
        pocket_dict1[idx] = val
        pocket_dict2[val] = idx

    for _ in range(M):
        val = sys.stdin.readline().strip()
        if val.isdigit():
            print(pocket_dict1[int(val)])
        else:
            print(pocket_dict2.get(val))


main()
