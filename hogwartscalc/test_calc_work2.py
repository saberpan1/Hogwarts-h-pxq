from hogwartscalc.calc_work import Calc
import pytest
import yaml


def get_yml(name):
    """
    获取yaml的列表
    :param name: yaml的key名称
    :return: 返回指定列表
    """
    return yaml.safe_load(open("./data.yml"))[name]


@pytest.mark.usefixtures("start", "calc")
class Testcalc:

    @pytest.mark.parametrize("a,b,expected",
                             get_yml("add_datas"),
                             ids=get_yml("myid"))
    def test_add(self, a, b, expected, calc):
        assert calc.add(a, b) == expected

    @pytest.mark.parametrize("a,b,expected",
                             get_yml("sub_datas"),
                             ids=get_yml("myid"))
    def test_sub(self, a, b, expected, calc):
        assert calc.sub(a, b) == expected

    @pytest.mark.parametrize("a,b,expected",
                             get_yml("mul_datas"),
                             ids=get_yml("myid"))
    def test_mul(self, a, b, expected, calc):
        assert calc.mul(a, b) == expected

    @pytest.mark.run(order=-1)
    @pytest.mark.parametrize("a,b,expected",
                             get_yml("div_datas"),
                             ids=get_yml("myid"))
    def test_div(self, a, b, expected, calc):
        assert calc.div(a, b) == expected
