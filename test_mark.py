import pytest

class Test_demo:

    @pytest.mark.demo
    def test_demo(self):
        print("我的第一个用例")

    @pytest.mark.login
    def test_login(self):
        print("我的登录用例")

    @pytest.mark.demo
    @pytest.mark.smoke
    def test_smoke(self):
        print("我的冒烟用例")


"""
pytest -v 显示用例名称，不显示print内容
pytest -s 显示print内容
pytest -x 有fail就停止执行
pytest --maxfail=3 fail等于3个时停止执行
pytest -sv -m  "demo or smoke" 执行标签包含demo或 smoke的用例

pytest -sv -m "demo and smoke" 执行标签同时包括demo和smoke的用例
pytest -sv -k "smoke" test_mark.py 执行方法名包含smoke的用例
pytest --collect-only test_mark.py 只收集用例，只会把用例名打印出来
"""
