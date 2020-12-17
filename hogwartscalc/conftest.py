import pytest
from hogwartscalc.calc_work import Calc


@pytest.fixture()
def start():
    print('开始计算')
    yield Calc()
    print('结束计算')


@pytest.fixture(scope="module")
def calc():
    return Calc()


def pytest_collection_modifyitems(session, config, items):
    print(type(items))
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
