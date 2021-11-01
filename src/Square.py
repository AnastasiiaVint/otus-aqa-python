from src.Base import Figure


class Square(Figure):
    _name = "Square"

    def __init__(self, side):
        if side > 0:
            self.a = side
        else:
            raise ValueError("Figure's side cannot be 0 or negative")

    @property
    def area(self):
        return self.a ** 2

    @property
    def perimeter(self):
        return self.a * 4

    def __repr__(self):
        return f"Square: {self.a} cm side"
