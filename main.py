from game import Game

if __name__ == "__main__":
    i = input(
        "Which difficulty do you want to play against? " +
        "[1: Play against a friend (default); 2: Easy; 3: Hard]: ")
    match i:
        case "1":
            game = Game(1, 1)
        case "2":
            game = Game(1, 2)
        case "3":
            game = Game(1, 3)
        case other:
            game = Game(1, 1)

    print("\n")
    game.start()
