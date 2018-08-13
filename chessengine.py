import chess
import chess.svg
from IPython.display import SVG

board = chess.Board("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
squares = board.attacks(chess.E4)
SVG(chess.svg.board(board=board, squares=squares)) 
print(board)
