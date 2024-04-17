from game.entities import Player


def main():
    player = Player.Player(10, 10, 10, 10, 10, 10)
    print(player.__str__())


if __name__ == "__main__":
    main()
