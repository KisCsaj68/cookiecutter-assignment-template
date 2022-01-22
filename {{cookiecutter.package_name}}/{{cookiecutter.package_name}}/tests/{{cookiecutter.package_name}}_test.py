from typing import Any, Tuple, List
from {{cookiecutter.package_name}}.{{cookiecutter.package_name}}.{{cookiecutter.package_name}} import \
    hello
import pytest


test_param: List[Tuple[str, str]] = [
    ("Viki","Hello Viki!"),
    ("","Hello World!")
    ]


@pytest.mark.parametrize("input, output", test_param)
def test_param(input, output):
    assert hello(input) == output
