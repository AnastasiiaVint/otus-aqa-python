import pytest

from src.Circle import Circle


@pytest.mark.parametrize("radius", [4, 6, 7, 11])
def test_circle_creation(radius):
    """Verify the circle object is created"""
    assert Circle(radius)


@pytest.mark.parametrize("radius", [-1, 0])
def test_circle_creation_negative(radius):
    """Verify the circle object cannot be created"""
    with pytest.raises(ValueError):
        Circle(radius)


def test_circle_name(circle):
    """Verify circle's object has a name"""

    assert circle.name == "Circle"


@pytest.mark.parametrize(
    "radius, area",
    [
        (2, 12.56),
        (1.5, 7.065),
        (3, 28.26),
    ]
)
def test_circle_area(radius, area):
    """Verify circle area is calculated correctly"""

    circle = Circle(radius)
    assert circle.area == area


@pytest.mark.parametrize(
    "radius, perimeter",
    [
        (2, 12.56),
        (1.5, 9.42),
        (3, 18.84),
    ]
)
def test_circle_perimeter(radius, perimeter):
    """Verify circle perimeter is calculated correctly"""

    circle = Circle(radius)
    assert circle.perimeter == perimeter


def test_circle_add_area(circle, square):
    """Verify circle can add area of another figure"""

    assert circle.add_area(square) == circle.area + square.area


def test_circle_add_area_not_figure(circle, fake_class):
    """Verify circle cannot add area from not figure"""

    with pytest.raises(ValueError):
        circle.add_area(fake_class)
