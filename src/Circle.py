from src.Base import Figure


class Circle(Figure):
    _name = "Circle"
    __pi_value = 3.14

    def __init__(self, radius):
        if radius > 0:
            self.r = radius
        else:
            raise ValueError("Figure's radius cannot be 0 or negative")

    @property
    def area(self):
        return self.__pi_value * (self.r ** 2)

    @property
    def perimeter(self):
        return 2 * self.__pi_value * self.r

    def __repr__(self):
        return f"Circle: {self.r} cm radius"
