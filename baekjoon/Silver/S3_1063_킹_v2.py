import sys
# sys.stdin = open('input.txt', 'r')

move_map = {
    "R": [0, 1],
    "L": [0, -1],
    "B": [1, 0],
    "T": [-1, 0],
    "RT": [-1, 1],
    "LT": [-1, -1],
    "RB": [1, 1],
    "LB": [1, -1]
}

def move_chess(piece_r, piece_c, move):
    return piece_r + move_map[move][0], piece_c + move_map[move][1]

def is_valid_position(r, c):
    return 0 <= r < 8 and 0 <= c < 8

def main():
    king, stone, N = sys.stdin.readline().split()
    N = int(N)

    king_r = 8 - int(king[1])
    king_c = ord(king[0]) - 65

    stone_r = 8 - int(stone[1])
    stone_c = ord(stone[0]) - 65

    for _ in range(N):
        move = sys.stdin.readline().strip()
        tmp_king_r, tmp_king_c = move_chess(king_r, king_c, move)
        if tmp_king_r == stone_r and tmp_king_c == stone_c:
            tmp_stone_r, tmp_stone_c = move_chess(stone_r, stone_c, move)
            if is_valid_position(tmp_stone_r, tmp_stone_c):
                stone_r = tmp_stone_r
                stone_c = tmp_stone_c
            else:
                continue

        if is_valid_position(tmp_king_r, tmp_king_c):
            king_r = tmp_king_r
            king_c = tmp_king_c

    print(f'{chr(king_c+65)}{8-king_r}')
    print(f'{chr(stone_c+65)}{8-stone_r}')

if __name__ == '__main__':
    main()

