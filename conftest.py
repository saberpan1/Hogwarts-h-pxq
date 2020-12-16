import pytest

'''
scope="session" 跨文件只执行一次
scope="module" 在py文件中开始时只执行一次
scope="class" 在class类中只执行一次
scope="function" 在每个测试用例开始时执行一次
'''


@pytest.fixture(params=["***param1***", "***param2***"])
def myfixture(request):
    print("执行我的fixture,里面的参数是\n", request.param)
    yield request.param
    print("激活fixture里的teardown操作")

# def connectdb():
#     print("执行我的fixture--connectdb")
