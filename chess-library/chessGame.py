import chess

board = chess.Board()

moves = ["e4", "e5", "Bc4", "Nc6", "Qf3", "d6", "Qf7"]

for i in moves:
    board.push_san(i)
print(board)
print(board.legal_moves)

