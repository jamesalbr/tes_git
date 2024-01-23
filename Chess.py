import chess
import chess.svg
from IPython.display import SVG, display

def display_board(board):
    display(SVG(chess.svg.board(board=board)))

def play_chess():
    board = chess.Board()

    while not board.is_game_over():
        display_board(board)
        print("Current FEN:", board.fen())
        move_uci = input("Enter your move (in UCI format, e.g., e2e4): ")
        
        try:
            move = chess.Move.from_uci(move_uci)
            if move in board.legal_moves:
                board.push(move)
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Use UCI format (e.g., e2e4).")

    display_board(board)
    print("Game Over. Result:", board.result())

if __name__ == "__main__":
    play_chess()
    