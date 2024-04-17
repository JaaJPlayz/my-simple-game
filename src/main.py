from game.entities import Monster, Player


def main():
    player = Player.Player(10, 10, 10, 10, 10, 10)
    monster = Monster.Monster(10, 10, 10, 10, 10, 10)
    print(player.__str__())
    print(monster.__str__())


if __name__ == "__main__":
    main()
