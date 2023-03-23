from abc import ABC, abstractmethod


class Character(ABC):
    """Class <Character(ABC)>"""
    @abstractmethod
    def __init__(self, name):
        """Create a Character"""
        self.first_name = name
        self.is_alive = True

    def die(self):
        """The Character dies abruptly like everyone \
in this show, don't get attached to quick..."""
        self.is_alive = False


class Stark(Character):
    """class Starck: the most northern family"""
    def __init__(self, name):
        """Winter is coming..."""
        super().__init__(name)
