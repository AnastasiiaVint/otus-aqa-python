

class Figure:
    _name = None

    def add_area(self, other):
        if isinstance(other, Figure):
            return self.area + other.area
        raise ValueError(f"The given {other} value is not a figure")

    @property
    def name(self):
        return self._name
