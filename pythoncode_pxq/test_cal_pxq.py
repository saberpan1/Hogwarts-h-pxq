import pytest

from pythoncode_pxq.calculator import Calculator


class TestCal:

    def setup_class(self):
        self.cal = Calculator()
        print("开始计算")

    @pytest.mark.parametrize("a,b,expect", [(1, 2, 3)])
    def test_add(self, a, b, expect):
        assert expect == self.cal.add(a, b)

    @pytest.mark.parametrize("a,b,expect", [(3, 2, 1)])
    def test_sub(self, a, b, expect):
        assert expect == self.cal.sub(a, b)
