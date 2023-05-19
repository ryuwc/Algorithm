import sys

def main():
    N = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    sorted_nums = sorted(set(nums))
    num_to_index = {num: idx for idx, num in enumerate(sorted_nums)}
    print(" ".join(str(num_to_index[num]) for num in nums))

if __name__ == '__main__':
    main()