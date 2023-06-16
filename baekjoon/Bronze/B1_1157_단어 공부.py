import sys
from collections import defaultdict


def main():
    words = sys.stdin.readline().strip().upper()

    dic = defaultdict(int)

    for word in words:
        dic[word] += 1

    max_cnt = max(dic.values())
    max_words = [word for word, cnt in dic.items() if cnt == max_cnt]

    print(max_words[0]) if len(max_words) == 1 else print('?')


if __name__ == '__main__':
    main()
