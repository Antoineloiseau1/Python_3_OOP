from abc import ABC, abstractmethod


class Character(ABC):
    """Class <Character(ABC)>"""
    @abstractmethod
    def __init__(self, name):
        """Create a Character"""
        self.first_name = name
        self.is_alive = True

    def die(self):
        """Kill the character"""
        self.is_alive = False


class Stark(Character):
    """Class <Stark(Character)>"""
    def __init__(self, name):
        """Create a member of Stark Family"""
        super().__init__(name)
