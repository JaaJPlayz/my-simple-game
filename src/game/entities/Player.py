class Player(object):
    """
    Player class

    Attributes:
        life (int): Player life
        mana (int): Player mana
        max_life (int): Player max life
        max_mana (int): Player max mana
        attack (int): Player attack
        defense (int): Player defense

    Methods:
        __init__(self, life, mana, max_life, max_mana, attack, defense)
        life(self)
        mana(self)
        max_life(self)
        max_mana(self)
        attack(self)
        defense(self)
        __str__(self)
        __repr__(self)
        __eq__(self, other)
        __ne__(self, other)
    """

    def __init__(self, life, mana, max_life, max_mana, attack, defense):
        self.__life = life
        self.__mana = mana
        self.__max_life = max_life
        self.__max_mana = max_mana
        self.__attack = attack
        self.__defense = defense

    # Getters
    @property
    def life(self):
        return self.__life

    @property
    def mana(self):
        return self.__mana

    @property
    def max_life(self):
        return self.__max_life

    @property
    def max_mana(self):
        return self.__max_mana

    @property
    def attack(self):
        return self.__attack

    @property
    def defense(self):
        return self.__defense

    # Setters
    @life.setter
    def life(self, life):
        self.__life = life

    @mana.setter
    def mana(self, mana):
        self.__mana = mana

    @max_life.setter
    def max_life(self, max_life):
        self.__max_life = max_life

    @max_mana.setter
    def max_mana(self, max_mana):
        self.__max_mana = max_mana

    @attack.setter
    def attack(self, attack):
        self.__attack = attack

    @defense.setter
    def defense(self, defense):
        self.__defense = defense

    # Methods
    def __str__(self):
        return f"life: {self.__life}, \
        mana: {self.__mana}, \
        max_life: {self.__max_life}, \
        max_mana: {self.__max_mana}, \
        attack: {self.__attack}, \
        defense: {self.__defense}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __ne__(self, other):
        return self.__str__() != other.__str__()
