__author__ = 'matt'


def is_winner(board):
    lines = [board[0:3],
             board[3:6],
             board[6:9],
             board[0:9:3],
             board[1:9:3],
             board[2:9:3],
             [board[0], board[4], board[8]],
             [board[2], board[4], board[6]]
             ]
    for line in lines:
        if abs(sum(line)) == 3:
            return True
    return False


n_games = int(raw_input())
#n_games = 1


for i in range(n_games):
    board = [0] * 9
    moves = [int(j) for j in raw_input().split()]
    #moves = [5,1,2,8,6,4,7,3,9]
    owner = {}
    order = {}
    winning_move = 0
    for j, move in enumerate(moves):
        player = (-1)**j
        board[move-1] = player
        if is_winner(board):
            winning_move = j+1
            break
    print winning_move,