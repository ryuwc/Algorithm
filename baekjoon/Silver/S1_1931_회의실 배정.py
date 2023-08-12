import sys

sinput = sys.stdin.readline


def main():
    N = int(sinput().rstrip())
    meetings = []
    for _ in range(N):
        a, b = map(int, sinput().rstrip().split())
        meetings.append([a, b])

    sorted_meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

    last_end_time = 0
    count = 0

    for start, end in sorted_meetings:
        if start >= last_end_time:
            count += 1
            last_end_time = end

    print(count)


main()
