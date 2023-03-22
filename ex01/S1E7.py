from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon Family"""
    def __init__(self, name):
        self.first_name = name
        self.is_alive = True
        self.family_name = self.__class__.__name__
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        return

    def __repr__(self) -> str:
        return 'Vector: ' + \
            str((self.family_name, self.eyes, self.hairs))


class Lannister(Character):
    """Representing the Baratheon Family"""
    def __init__(self, name):
        self.first_name = name
        self.is_alive = True
        self.family_name = self.__class__.__name__
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        return

    def __repr__(self) -> str:
        return 'Vector: ' + \
            str((self.family_name, self.eyes, self.hairs))

    @classmethod
    def create_lannister(cls, name, is_alive):
        new_born = cls(name)
        new_born.is_alive = is_alive
        return new_born
