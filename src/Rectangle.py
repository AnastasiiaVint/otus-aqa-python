from src.Base import Figure


class Rectangle(Figure):
    _name = "Rectangle"

    def __init__(self, width, length):
        if width > 0 and length > 0:
            self.a = width
            self.b = length
        else:
            raise ValueError("Figure's side cannot be 0 or negative")

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return (self.a + self.b) * 2

    def __repr__(self):
        return f"Rectangle: {self.a} cm, {self.b} cm"
