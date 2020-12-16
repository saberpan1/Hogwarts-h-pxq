import pytest
from pythoncode_pxq.calculator import Calculator


@pytest.fixture(scope="module")
def start():
    cal = Calculator
    print("开始计算")
    return cal
