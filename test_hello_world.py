import pytest

from hello_world import get_max_element


@pytest.fixture(autouse=True)
def xxx():
    print("前置条件")
    yield
    print("清理操作")


def test_get_max_element():
    """
    这是单元测试
    :return:
    """
    print("测试步骤 test_get_max_element")
    list_to_test = [-12, -3, -9, -8, -56]
    expected = -3
    actual = get_max_element(list_to_test)
    assert expected == actual, "这是 pytest 单元测试"

def test_get_max_element2():
    """
    这是单元测试
    :return:
    """
    print("测试步骤 test_get_max_element2")
    list_to_test = [-12, -3, -9, -8, -56]
    expected = -3
    actual = get_max_element(list_to_test)
    assert expected == actual, "这是 pytest 单元测试"
