import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.fixture()
def circle():
    circle_figure = Circle(5)
    yield circle_figure
    del circle_figure


@pytest.fixture()
def triangle():
    triangle_figure = Triangle(3, 4, 5)
    yield triangle_figure
    del triangle_figure


@pytest.fixture()
def square():
    square_figure = Square(7)
    yield square_figure
    del square_figure


@pytest.fixture
def rectangle():
    rectangle_figure = Rectangle(6, 8)
    yield rectangle_figure
    del rectangle_figure


@pytest.fixture
def fake_class():
    class Test:
        pass
    not_figure = Test()
    yield not_figure
    del not_figure
