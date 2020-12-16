import pytest

from pythoncode_pxq.calculator import Calculator


@pytest.fixture(scope="function")
def start():
    Calc = Calculator()
    print("开始计算")
    return Calc


class TestCal:

    @pytest.mark.parametrize("a,b,expect", [(1, 2, 3)], start)
    def test_add(self, a, b, expect):
        assert expect == self.cal.add(a, b)

    @pytest.mark.parametrize("a,b,expect", [(3, 2, 1)])
    def test_sub(self, a, b, expect):
        assert expect == self.cal.sub(a, b)
