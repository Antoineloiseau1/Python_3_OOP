class calculator:
    """class calculator allow to do product, \
addition and substraction of two vectors"""
    def __init__(self) -> None:
        """__init__ constructor function"""
        pass

    @classmethod
    def dotproduct(self, V1, V2) -> None:
        """Do a dot product of Vector 1 and Vector2"""
        print("Dot product is:", sum([x * y for x, y in zip(V1, V2)]))

    @classmethod
    def add_vec(self, V1, V2) -> None:
        """Do an addition of Vector 1 and Vector2"""
        print("Add Vector is:", list([float(x + y) for x, y in zip(V1, V2)]))

    @classmethod
    def sous_vec(self, V1, V2) -> None:
        """Do a substraction of Vector 1 and Vector2"""
        print("Add Vector is:", list([float(x - y) for x, y in zip(V1, V2)]))
