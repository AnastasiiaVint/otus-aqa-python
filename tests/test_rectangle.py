import pytest

from src.Rectangle import Rectangle


@pytest.mark.parametrize(
    "a, b",
    [
        (3, 5),
        (4, 9),
        (1, 2),
    ]
)
def test_rectangle_creation(a, b):
    """Verify the rectangle object is created"""
    assert Rectangle(a, b)


@pytest.mark.parametrize(
    "a, b",
    [
        (-3, 5),
        (4, 0),
    ]
)
def test_rectangle_creation_negative(a, b):
    """Verify the rectangle object cannot be created"""
    with pytest.raises(ValueError):
        Rectangle(a, b)


def test_rectangle_name(rectangle):
    """Verify rectangle's object has a name"""

    assert rectangle.name == "Rectangle"


@pytest.mark.parametrize(
    "a, b, area",
    [
        (3, 5, 15),
        (4, 9, 36),
        (1, 2, 2),
    ]
)
def test_rectangle_area(a, b, area):
    """Verify rectangle area is calculated correctly"""

    rectangle = Rectangle(a, b)
    assert rectangle.area == area


@pytest.mark.parametrize(
    "a, b, perimeter",
    [
        (3, 5, 16),
        (4, 9, 26),
        (1, 2, 6),
    ]
)
def test_rectangle_perimeter(a, b,  perimeter):
    """Verify rectangle perimeter is calculated correctly"""

    rectangle = Rectangle(a, b)
    assert rectangle.perimeter == perimeter


def test_rectangle_add_area(rectangle, triangle):
    """Verify rectangle can add area of another figure"""

    assert rectangle.add_area(triangle) == rectangle.area + triangle.area


def test_rectangle_add_area_not_figure(rectangle, fake_class):
    """Verify rectangle cannot add area from not figure"""

    with pytest.raises(ValueError):
        rectangle.add_area(fake_class)
