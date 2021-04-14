# -*- coding: utf-8 -*-
# @Author  : danchaofan

import pytest
import os
import yaml
from pathlib import Path


# 读取测试数据
def get_datas(file_name, func_name):
    # 获取测试数据的绝对路径
    parent_path = Path(__file__).absolute().parents[1]
    path = Path.joinpath(parent_path, "testdata", file_name)
    with open(path, encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        func_datas = datas[func_name]['datas']
        ids = datas[func_name]['ids']
    return [func_datas, ids]


@pytest.fixture(params=get_datas("test_data.yml", "add")[0], ids=get_datas("test_data.yml", "add")[1])
def get_add_datas(request):
    return request.param


@pytest.fixture(params=get_datas("test_data.yml", "divide")[0], ids=get_datas("test_data.yml", "divide")[1])
def get_divide_datas(request):
    return request.param


@pytest.fixture(params=get_datas("test_data.yml", "subtract")[0], ids=get_datas("test_data.yml", "subtract")[1])
def get_subtract_datas(request):
    return request.param


@pytest.fixture(params=get_datas("test_data.yml", "multiply")[0], ids=get_datas("test_data.yml", "multiply")[1])
def get_multiply_datas(request):
    return request.param

