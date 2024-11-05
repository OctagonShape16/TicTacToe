from ai import MiniMax, RandomMove

class Board:
    "represents physical board"
    def __init__(self):
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def sign_to_printable(self, sign):
        match sign:
            case 1:
                return "X"
            case 2:
                return "O"
            case 0:
                return " "

    def print_board(self):
        print(" " + self.sign_to_printable(self.state[0]) + " | " +
              self.sign_to_printable(self.state[1]) + " | " +
              self.sign_to_printable(self.state[2]) + " \n" +
              " ---------\n" +
              " " + self.sign_to_printable(self.state[3]) + " | " +
              self.sign_to_printable(self.state[4]) + " | " +
              self.sign_to_printable(self.state[5]) + " \n" +
              " ---------\n" +
              " " + self.sign_to_printable(self.state[6]) + " | " +
              self.sign_to_printable(self.state[7]) + " | " +
              self.sign_to_printable(self.state[8]) + " \n")

    def is_full(self):
        for i in self.state:
            if i == 0:
                return False
        return True

    def check_win(self, symbol):
        s = symbol
        if self.state[0] == s and self.state[1] == s and self.state[2] == s:
            return True
        elif self.state[3] == s and self.state[4] == s and self.state[5] == s:
            return True
        elif self.state[6] == s and self.state[7] == s and self.state[8] == s:
            return True

        elif self.state[0] == s and self.state[3] == s and self.state[6] == s:
            return True
        elif self.state[1] == s and self.state[4] == s and self.state[7] == s:
            return True
        elif self.state[2] == s and self.state[5] == s and self.state[8] == s:
            return True

        elif self.state[0] == s and self.state[4] == s and self.state[8] == s:
            return True
        elif self.state[2] == s and self.state[4] == s and self.state[6] == s:
            return True

    def make_move(self, cell, symbol):
        if self.check_move(cell):
            self.state[cell] = symbol

    def check_move(self, cell):
        if self.state[cell] == 0:
            return True
        else:
            return False

class Player:
    def __init__(self, symbol):
            self.symbol = symbol
            self.tag = "p"

class Game:
    "main game loop"
    def __init__(self, id, mode):
        self.id = id
        self.mode = mode
        self.done = False
        self.board = Board()
        if self.mode >= 2:
            if self.mode == 2:
                self.ai = RandomMove()
            elif self.mode == 3:
                self.ai = MiniMax()
            self.player1 = Player(1 if self.ai.symbol == 2 else 2)
            self.current_player = self.ai if self.ai.symbol == 1 else self.player1
        else:
            self.player1 = Player(1)
            self.current_player = self.player1
        self.player2 = Player(2)

        print(" 1 | 2 | 3 \n --------- \n 4 | 5 | 6 \n --------- \n 7 | 8 | 9")

    def start(self):
        while not self.done:
            if self.board.is_full():
                print("It's a tie!")
                self.done = True
                break

            if self.current_player.tag == "ai":
                move = self.ai.make_move(self.board)
                print(
                    f"AI chooses position {move + 1}, " +
                     f"after looking at {self.ai.count} different games\n")
                move = str(move + 1)
                self.ai.count = 0
            else:
                move = input(
                    f"Player {self.current_player.symbol}, make your move (1-9): ")

            if move.isdigit():
                move = int(move)
                if 1 <= move <= 9:
                    move -= 1
                    if self.board.check_move(move):
                        self.board.make_move(move, self.current_player.symbol)
                        if self.board.check_win(self.current_player.symbol):
                            self.board.print_board()
                            if self.mode == 1:
                                print(f"Player {self.current_player.symbol} wins!")
                            else:
                                if self.current_player.tag == "ai":
                                    print("AI wins!")
                                else:
                                    print("You win!")
                            self.done = True
                        else:
                            if self.mode == 1:
                                self.current_player = (self.player2
                                                       if self.current_player ==
                                                       self.player1
                                                       else self.player1)
                            else:
                                self.current_player = (self.player1
                                                       if self.current_player == self.ai
                                                       else self.ai)
                    else:
                        print("Invalid move. Try again.")
                else:
                    print("Input must be a number between 1 and 9. Try again.")
            else:
                print("Invalid input. Try again.")

            if not self.done:
                self.board.print_board()
