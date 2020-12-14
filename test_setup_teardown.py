import pytest

def setup_model():
    print("setup:整个py文件模块只执行一次")


def teardown_model():
    print("teardown:整个py文件模块只执行一次")


def setup_function():
    print("setup:不在类中的测试用例开始的时候都会执行")


def teardown_function():
    print("teardown:不在类中的测试用例结束的时候都会执行")


def test_three():
    print("test_three")


def test_four():
    print("test_four")


class TestClass():
    def setup_class(self):
        print("类中开始执行一次")

    def teardown_class(self):
        print("类中结束执行一次")

    def setup_method(self):
        print("开始")

    def teardown_method(self):
        print("结束")

    def test_one(self):
        print("test-one")

    def test_two(self):
        print("test-two")
