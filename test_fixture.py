import pytest


class Test_demo():
    def test_one(self, myfixture):
        print("执行test_one")
        assert 1 + 1 == 2


class Test_demo3():
    def test_one3(self):
        print("执行test_one3")
        assert 1 + 1 == 2
