class calculator():
    """class calculator: allows to add, sub, multiply and divide"""
    def __init__(self, numbers: list) -> None:
        """Create an instance of calculator"""
        self.numbers = numbers

    def __add__(self, object) -> None:
        """Add object to numbers"""
        self.numbers = [i + object for i in self.numbers]
        print([i for i in self.numbers])

    def __mul__(self, object) -> None:
        """Multiply numbers by object"""
        self.numbers = [i * object for i in self.numbers]
        print([i for i in self.numbers])

    def __sub__(self, object) -> None:
        """Substract object to numbers"""
        self.numbers = [i - object for i in self.numbers]
        print([i for i in self.numbers])

    def __truediv__(self, object) -> None:
        """Divide numbers by object"""
        try:
            self.numbers = [i / object for i in self.numbers]
            print([i for i in self.numbers])
        except ZeroDivisionError as msg:
            print("ZeroDivisionError:", msg)
