import sys

sinput = sys.stdin.readline


def is_all_same(sr, sc, er, ec):
    color = papers[sr][sc]
    for i in range(sr, er):
        for j in range(sc, ec):
            if papers[i][j] != color:
                return False

    return True


def solve(sr, sc, er, ec):
    if is_all_same(sr, sc, er, ec):
        paper_dict[papers[sr][sc]] += 1
        return

    mid_r = (sr + er) // 2
    mid_c = (sc + ec) // 2

    solve(sr, sc, mid_r, mid_c)
    solve(sr, mid_c, mid_r, ec)
    solve(mid_r, sc, er, mid_c)
    solve(mid_r, mid_c, er, ec)


N = int(sinput().rstrip())
papers = [list(map(int, sinput().rstrip().split())) for _ in range(N)]
paper_dict = {0: 0, 1: 0}

solve(0, 0, N, N)
print(paper_dict.get(0))
print(paper_dict.get(1))
