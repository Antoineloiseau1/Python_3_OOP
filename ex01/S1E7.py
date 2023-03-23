from S1E9 import Character


class Baratheon(Character):
    """class Baratheon: They really are the true kings"""
    def __init__(self, name):
        """Ours is the fury"""
        self.first_name = name
        self.is_alive = True
        self.family_name = self.__class__.__name__
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        """Tells what are the caracteristics of Baratheon family"""
        return

    def __repr__(self) -> str:
        """Tells what are the caracteristics of Baratheon family"""
        return 'Vector: ' + \
            str((self.family_name, self.eyes, self.hairs))


class Lannister(Character):
    """class Lannister: The king makers"""
    def __init__(self, name):
        """Lannisters always pay their debts"""
        self.first_name = name
        self.is_alive = True
        self.family_name = self.__class__.__name__
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        """Tells what are the caracteristics of Lannister family"""
        return

    def __repr__(self) -> str:
        """Tells what are the caracteristics of Lannister family"""
        return 'Vector: ' + \
            str((self.family_name, self.eyes, self.hairs))

    @classmethod
    def create_lannister(cls, name, is_alive):
        """Legimately create a new member of the Lannister family"""
        new_born = cls(name)
        new_born.is_alive = is_alive
        return new_born
