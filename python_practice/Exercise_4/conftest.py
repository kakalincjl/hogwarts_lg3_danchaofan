# -*- coding: utf-8 -*-
# @Author  : danchaofan

from typing import List

import pytest


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print("Config", config)
    all_items = []
    divide_itesms = []
    add_itesms = []
    multiply_itesms = []
    subtract_itesms = []
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        print("item._nodeid:", item._nodeid)
        print("item.keywords:", item.keywords.__dict__['_markers'])
        print("item.own_markers:", item.own_markers)
        print("item.ihook:", item.ihook)
        print("item.fspath:", item.fspath)
        print("item.extra_keyword_matches:", item.extra_keyword_matches)

    #     if item.name.startswith("test_divide"):
    #         divide_itesms.append(item)
    #     elif item.name.startswith("test_multiply"):
    #         multiply_itesms.append(item)
    #     elif item.name.startswith("test_add"):
    #         add_itesms.append(item)
    #     else:
    #         subtract_itesms.append(item)
    # all_items.append(add_itesms)
    # all_items.append(multiply_itesms)
    # all_items.append(divide_itesms)
    # all_items.append(subtract_itesms)
    # print('>>>>>>>>>>>>>>>>>>', all_items)
    # # items[:] = all_items
    # for i in all_items:
    #     item = i
    #     yield item


@pytest.fixture(scope='module', autouse=True)
def cal_print():
    print('开始计算')
    yield
    print('计算结束')
