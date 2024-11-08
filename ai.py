import math
import copy
import random
from prompt import get_completion, create_message

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

    def change_symbol(self):
        self.symbol = 1 if self.symbol == 2 else 2

    def make_move(self, board):
        pass

class Minimax(AI):
    "move generation using minimax algorithm"
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

class RandomMove(AI):
    "generates random move"
    def __init__(self):
        super().__init__()

    def make_move(self, board):
        move = random.choice(self.get_moves(board))
        return move

class LLM(AI):
    "move generation using a Large Language Model"
    def __init__(self):
        super().__init__()

    def make_move(self, board):
        message = create_message(self.convert_json(board))
        move = get_completion(message)
        move = int(move)
        return move - 1

    def convert_json(self, board):
        json_board = {f"{i+1}":item for i, item in enumerate(board.state)}
        json_board["moves"] = f"{[j + 1 for j in self.get_moves(board)]}"
        json_board["symbol"] = f"{self.symbol}"
        return json_board
