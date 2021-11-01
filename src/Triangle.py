from math import sqrt

from src.Base import Figure


class Triangle(Figure):
    _name = "Triangle"

    def __init__(self, first_side, second_side, third_side):
        self.a = first_side
        self.b = second_side
        self.c = third_side

    @property
    def area(self):
        """Calculating the area of a triangle.

        p is half of the perimeter of the triangle
        s is an area
        """

        p = self.perimeter / 2
        s = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return s

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    def __repr__(self):
        return f"Triangle: {self.a} cm, {self.b} cm, {self.c} cm"

    def __new__(cls, *args):
        max_side = max(args)
        side_sum = sum(args)

        if (side_sum - max_side) <= max_side:
            return None
        return super(Triangle, cls).__new__(cls)
