import allure
import pytest


@allure.feature("搜索模块")
class TestSearch:

    def test_one(self):
        print("用例1")

    def test_two(self):
        print("用例2")


@allure.feature("登录模块")
class TestLogin:

    @allure.story("登录成功")
    def test_login_success(self):
        print("这是登录：测试用例，登录成功")
        pass

    @allure.story("登录失败")
    def test_login_fail(self):
        print("这是登录：测试用例，登录失败")
        pass
