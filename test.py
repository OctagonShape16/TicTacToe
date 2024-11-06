from ai import Minimax, RandomMove
from game import Board

class Test:
    "used to let 2 AIs play against each other"
    def __init__(self, id, engine):
        self.id = id
        self.engine = engine # 1 = random move; 3 = minimax; TODO: 2 = LLM
        self.done = False
        self.outcome = None
        self.board = Board()
        if engine == 1:
            self.player1 = RandomMove()
        elif engine == 2:
            self.player1 = RandomMove()
        elif engine == 3:
            self.player1 = Minimax()
        self.player2 = RandomMove()
        if self.player1.symbol == self.player2.symbol:
            self.player2.change_symbol()
        if self.player1.symbol == 1:
            self.current_player = self.player1
        else:
            self.current_player = self.player2

    def start(self):
        while not self.done:
            if self.board.is_full():
                self.outcome = 0
                self.done = True
                break

            move = self.current_player.make_move(self.board)
            self.current_player.count = 0

            self.board.make_move(move, self.current_player.symbol)
            if self.board.check_win(self.current_player.symbol):
                if self.current_player == self.player1:
                    self.outcome = 1
                else:
                    self.outcome = 2
                self.done = True
            else:
                self.current_player = (self.player2
                                       if self.current_player ==
                                       self.player1
                                       else self.player1)
        return self.outcome

def benchmark(mode, iterations):
    """collects the date from a lot of AI games and
    calculates the win rate of the specific engine"""
    wins = 0
    for i in range(iterations):
        test = Test(i + 1, mode)
        if test.start() == 1:
            wins += 1
    percentage = "{:.2f}".format((wins / iterations) * 100)
    print(f"The AI won {percentage}% of the time against a random move generation")

if __name__ == "__main__":
    i = input(
        "Which AI do you want to test? " +
        "[1: Random Move generation; 2: LLM; 3: Minimax]: ")
    while not (i.isdigit() and 1 <= int(i) <= 3):
        print("Invalid input. Try again.")
        i = input(
        "Which AI do you want to test? " +
        "[1: Random Move generation; 2: LLM; 3: Minimax]: ")
    print("\n")
    j = input("For how many iterations do you want to test the AI?:")
    while not (i.isdigit() and 1 <= int(i)):
        print("Invalid input. Try again.")
        j = input("For how many iterations do you want to test the AI?:")
    j = int(j)
    match i:
        case "1":
            benchmark(1, j)
        case "2":
            benchmark(2, j)
        case "3":
            benchmark(3, j)
