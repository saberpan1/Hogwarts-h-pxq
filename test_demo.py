import pytest


def num_add(a, b):
    return a + b


@pytest.mark.parametrize("ass", [3, -3, 2000])
@pytest.mark.parametrize("a,b", [
    (1, 2), (-1, -2), (1000, 1000)])
def test_one(a, b, ass):
    print(f"测试用例组合a:{a},b:{b},ass:{ass}")
