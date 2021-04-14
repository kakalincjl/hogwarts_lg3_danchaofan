# -*- coding: utf-8 -*-
# @Author  : danchaofan

import sys
import pytest
import allure
from pathlib import Path

current_paths = Path(__file__).absolute().parents
parent_path = current_paths[1]
sys.path.append(str(parent_path))
sys.path.append('..')

from calculator import Calculator


@allure.feature("计算器模块")
class TestCal:

    def setup_class(self):
        self.calc = Calculator()

    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    @allure.story('测试计算器加法')
    @pytest.mark.add
    @pytest.mark.run(order=1)
    def test_add(self, get_add_datas):
        result = self.calc.add(get_add_datas[0], get_add_datas[1])
        assert get_add_datas[2] == result

    @allure.story('测试计算器减法')
    @pytest.mark.subtract
    @pytest.mark.run(order=-2)
    def test_subtract(self, get_subtract_datas):
        result = self.calc.subtract(get_subtract_datas[0], get_subtract_datas[1])
        assert get_subtract_datas[2] == result

    @allure.story('测试计算器乘法')
    @pytest.mark.multiply
    @pytest.mark.run(order=-1)
    def test_multiply(self, get_multiply_datas):
        result = self.calc.multiply(get_multiply_datas[0], get_multiply_datas[1])
        assert get_multiply_datas[2] == result

    @allure.story('测试计算器除法')
    @pytest.mark.divide
    @pytest.mark.run(order=2)
    def test_divide(self, get_divide_datas):
        result = self.calc.divide(get_divide_datas[0], get_divide_datas[1])
        assert get_divide_datas[2] == result
