from hogwartscalc.calc_work import Calc
import pytest


class Testcalc():
    def setup_class(self):
        self.calc = Calc()
        print('生成Calc实例')

    def setup_method(self):
        print("开始计算")

    def teardown_method(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expected", [(1, 2, 3), (-1, -2, -3), (1000, 2000, 3000)])
    def test_add(self, a, b, expected):
        assert self.calc.add(a, b) == expected

    @pytest.mark.parametrize("a,b,expected", [(1, 2, -1), (-1, -2, 1), (1000, 2000, -1000)])
    def test_sub(self, a, b, expected):
        assert self.calc.sub(a, b) == expected

    @pytest.mark.parametrize("a,b,expected", [(1, 2, 2), (-1, -2, 2), (1000, 2000, 2000000)])
    def test_mul(self, a, b, expected):
        assert self.calc.mul(a, b) == expected

    @pytest.mark.parametrize("a,b,expected", [(1, 2, 0.5), (-2, -1, 2), (1000, 2000, 0.5)])
    def test_div(self, a, b, expected):
        assert self.calc.div(a, b) == expected
