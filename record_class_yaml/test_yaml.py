import yaml
import pytest
import time

class TestYaml:

    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yml")))
    def test_one(self, env):
        if "test" in env:
            print("test环境")
            print("测试环境的ip是", env["test"])
        elif "dev" in env:
            print("dev环境")
            print("开发环境的ip是", env["dev"])