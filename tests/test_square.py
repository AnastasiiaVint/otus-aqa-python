import pytest

from src.Square import Square


@pytest.mark.parametrize("a", [4, 6, 7, 11])
def test_square_creation(a):
    """Verify the square object is created"""
    assert Square(a)


@pytest.mark.parametrize("a", [-1, 0])
def test_square_creation_negative(a):
    """Verify the square object cannot be created"""
    with pytest.raises(ValueError):
        Square(a)


def test_square_name(square):
    """Verify square's object has a name"""

    assert square.name == "Square"


@pytest.mark.parametrize(
    "a, area",
    [
        (2, 4),
        (1, 1),
        (0.5, 0.25),
    ]
)
def test_square_area(a, area):
    """Verify square area is calculated correctly"""

    square = Square(a)
    assert square.area == area


@pytest.mark.parametrize(
    "a, perimeter",
    [
        (2, 8),
        (1.5, 6),
        (3, 12),
    ]
)
def test_square_perimeter(a, perimeter):
    """Verify square perimeter is calculated correctly"""

    square = Square(a)
    assert square.perimeter == perimeter


def test_square_add_area(square, rectangle):
    """Verify square can add area of another figure"""

    assert square.add_area(rectangle) == square.area + rectangle.area


def test_circle_add_area_not_figure(square, fake_class):
    """Verify square cannot add area from not figure"""

    with pytest.raises(ValueError):
        square.add_area(fake_class)
