from typing import Any, Tuple, List
from {{cookiecutter.package_name}}.{{cookiecutter.package_name}}.{{cookiecutter.package_name}} import \
    max, min, divmod, multiply
import pytest


min_list: List[Tuple[int, int, int]] = [
    (5, 78, 5),
    (67, 3, 3),
    (-45, 5, -45),
    (5, 5, 5),
    (-87, -54, -87),
]
max_list: List[Tuple[List[int], int]] = [
    ([1, 2, 3], max([1, 2, 3])),
    ([1, 1, 1], max([1, 1, 1])),
    ([-32, 55, 678, 66, 67, 432], max([-32, 55, 678, 66, 67, 432])),
    ([-25, -45, -435], max([-25, -45, -435])),
    ([456, 678, 1234, 1234, 5, 6, 7], max([456, 678, 1234, 1234, 5, 6, 7]))
]

len_list: List[Tuple[List[Any], int]] = [
    ([1], len([1])),
    ([234, 456, 778], len([234, 456, 778])),
    ([], len([])),
    (["s", "t", "sfdsdfsd", "dddfe", "eeee"], len(
        ["s", "t", "sfdsdfsd", "dddfe", "eeee"])),
    (["a"], len(["a"]))

]

multiply_list: List[Tuple[int, int, int]] = [
    (3, 4, 12),
    (-3, 4, -12),
    (-3, -4, 12),
    (3, -4, -12)
]

pow_list: List[Tuple[int, int, int]] = [
    (2, 0, 1),
    (0, 2, 0),
    (2, 1, 2),
    (2, 2, 4),
    (2, 3, 8)
]

div_mod_list: List[Tuple[int, int, int, int]] = [
    (5, 5, 5//5, 5 % 5),
    (-5, -5, -5//-5, -5 % -5),
    (5, 2, 5//2, 5 % 2),
    (2, 5, 2//5, 2 % 5),
    (-5, 2, -5//2, -5 % 2),
    (-2, -5, -2 // -5, -2 % -5),
    (-5, -2, -5 // -2, -5 % -2),
    (5, -2, 5 // -2, 5 % -2)
]


@pytest.mark.parametrize("a, b, expected", min_list)
def test_min(a, b, expected):
    assert min(a, b) == expected


@pytest.mark.parametrize("a, expected", max_list)
def test_max(a, expected):
    assert max(a) == expected


@pytest.mark.parametrize("a, expected", len_list)
def test_len(a, expected):
    assert len(a) == expected


@pytest.mark.parametrize("a, b, expected", multiply_list)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", pow_list)
def test_pow(a, b, expected):
    assert pow(a, b) == expected


@pytest.mark.parametrize("a, b, c, d", div_mod_list)
def test_div(a, b, c, d):
    assert divmod(a, b) == (c, d)
