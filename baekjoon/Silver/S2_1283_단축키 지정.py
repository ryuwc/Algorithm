import sys


def main():
    N = int(sys.stdin.readline().strip())
    options = [sys.stdin.readline().strip() for _ in range(N)]
    alpha_set = set()

    for option in options:
        words = option.split()
        is_assigned = False
        # 첫 글자 확인
        for idx, word in enumerate(words):
            if word[0].lower() not in alpha_set:
                alpha_set.add(word[0].lower())
                words[idx] = '[' + word[0] + ']' + word[1:]
                is_assigned = True
                break

        # 첫 글자 모두 사용되었다면 다음 글자 확인
        if not is_assigned:
            for idx, word in enumerate(words):
                for i in range(1, len(word)):
                    if word[i].lower() not in alpha_set:
                        alpha_set.add(word[i].lower())
                        words[idx] = word[:i] + '[' + word[i] + ']' + word[i + 1:]
                        is_assigned = True
                        break
                if is_assigned:
                    break
        print(' '.join(words))


if __name__ == '__main__':
    main()
