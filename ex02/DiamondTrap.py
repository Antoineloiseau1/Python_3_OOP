from S1E7 import Lannister, Baratheon


class King(Baratheon, Lannister):
    """class King"""
    def __init__(self, name):
        """Everyone Is Mines To Torment."""
        super().__init__(name)

    def set_eyes(self, color):
        """Nothing like a Baratheon eyes"""
        self.eyes = color

    def set_hairs(self, color):
        """Nothing like a Baratheon hairs"""
        self.hairs = color

    def get_eyes(self):
        """Nothing like a Baratheon eyes"""
        return self.eyes

    def get_hairs(self):
        """Nothing like a Baratheon hairs"""
        return self.hairs
