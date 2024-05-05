import random


def find_empty_square(game_board):
    for i in range(4):
        for j in range(4):
            if game_board[i][j] == ' ':
                return i, j

def check_win(game_board):
    win_board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, ' ']]
    return game_board == win_board

def check_board(game_board,empty_i):
    pairs_sum = sum(game_board[:i].count(j) for i, j in enumerate(game_board, start=1) if j != 0 for j in range(1, i))
    total_sum = pairs_sum + (empty_i + 1)
    if total_sum % 2 == 0:
        return   1       # есть победное решение
    else:
        return   2       # нету победного решения

def random_board():
    while True:
        nums = list(range(1, 16))
        random.shuffle(nums)
        empty_index = random.randint(0, 15)
        nums.insert(empty_index, ' ')
        game_board = [nums[i:i+4] for i in range(0, 16, 4)]
        empty_i, empty_j = find_empty_square(game_board)
        if check_board(game_board, empty_i) == 1:
            return game_board    
game_board = random_board()

