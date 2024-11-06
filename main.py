from game import Game

if __name__ == "__main__":
    i = input(
        "Which difficulty do you want to play against? " +
        "[1: Play against a friend; 2: Easy; 3: Hard; 4: Impossible]: ")
    while not (i.isdigit() and 1 <= int(i) <= 4):
        print("Invalid input. Try again.")
        i = input(
        "Which difficulty do you want to play against? " +
        "[1: Play against a friend; 2: Easy; 3: Hard; 4: Impossible]: ")

    match i:
        case "1":
            game = Game(1, 1)
        case "2":
            game = Game(1, 2)
        case "3":
            game = Game(1, 3)
        case "4":
            game = Game(1, 4)

    print("\n")
    game.start()
