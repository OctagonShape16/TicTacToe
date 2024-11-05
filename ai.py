import math
import copy
import random

class AI:
    def __init__(self):
        self.symbol = random.randint(1, 2)
        self.tag = "ai"
        self.count = 0

    def get_moves(self, board):
        moves = []
        for i in range(0, 9):
            if board.check_move(i):
                moves.append(i)
        return moves
    
    def make_move(self, board):
        pass

# move generation using minimax algorithm
class MiniMax(AI):
    def __init__(self):
        super().__init__()
    
    def make_move(self, board):
        if self.symbol == 1:
            _, move = self.minimax(board, 9, -math.inf, math.inf, True)
        else:
            _, move = self.minimax(board, 9, -math.inf, math.inf, False)
        return move
    
    def minimax(self, board, depth, alpha, beta, is_maximizing):
        if board.check_win(1):
            self.count += 1
            return 10 + depth, None
        elif board.check_win(2):
            self.count += 1
            return -10 - depth, None
        elif board.is_full():
            self.count += 1
            return 0, None

        if is_maximizing:
            max_eval = -math.inf
            best_move = None
            for i in self.get_moves(board):
                temp_board = copy.deepcopy(board)
                temp_board.make_move(i, 1)
                eval, _ = self.minimax(temp_board, depth - 1, alpha, beta, False)
                if eval > max_eval:
                    max_eval = eval
                    best_move = i
                alpha = max(alpha, eval)
                if alpha >= beta:
                    break 
            return max_eval, best_move
        
        else:
            min_eval = math.inf
            best_move = None
            for i in self.get_moves(board):
                temp_board = copy.deepcopy(board)
                temp_board.make_move(i, 2)
                eval, _ = self.minimax(temp_board, depth - 1, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = i
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

# random move generation       
class RandomMove(AI):
    def __init__(self):
        super().__init__()

    def make_move(self, board):
        move = random.choice(self.get_moves(board))
        return move
