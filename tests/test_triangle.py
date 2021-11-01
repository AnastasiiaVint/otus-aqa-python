import pytest

from src.Triangle import Triangle


@pytest.mark.parametrize(
    "a, b, c",
    [
        (3, 4, 5),
        (5, 6, 10),
        (0.5, 7, 7),
    ]
)
def test_triangle_creation(a, b, c):
    """Verify the triangle object is created"""
    assert Triangle(a, b, c)


@pytest.mark.parametrize(
    "a, b, c",
    [
        (1, 4, 5),
        (2, -6, 10),
        (0.5, 1, 0),
    ]
)
def test_triangle_creation_negative(a, b, c):
    """Verify the triangle object return None if object cannot be created """

    assert Triangle(a, b, c) is None


def test_triangle_name(triangle):
    """Verify triangle's object has a name"""

    assert triangle.name == "Triangle"


@pytest.mark.parametrize(
    "a, b, c, area",
    [
        (3, 4, 5, 6),
        (6, 4, 2.5, 3.63),
        (1, 0.5, 0.6, 0.11),
    ]
)
def test_triangle_area(a, b, c, area):
    """Verify triangle area is calculated correctly"""

    triangle = Triangle(a, b, c)
    assert round(triangle.area, 2) == area


@pytest.mark.parametrize(
    "a, b, c, perimeter",
    [
        (3, 4, 5, 12),
        (6, 4, 2.5, 12.5),
        (1, 0.5, 0.6, 2.1),
    ]
)
def test_triangle_perimeter(a, b, c, perimeter):
    """Verify triangle perimeter is calculated correctly"""

    triangle = Triangle(a, b, c)
    assert triangle.perimeter == perimeter


def test_triangle_add_area(triangle, circle):
    """Verify triangle can add area of another figure"""

    assert triangle.add_area(circle) == triangle.area + circle.area


def test_triangle_add_area_not_figure(triangle, fake_class):
    """Verify triangle cannot add area from not figure"""

    with pytest.raises(ValueError):
        triangle.add_area(fake_class)
