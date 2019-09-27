import pytest
import csv
from hello_world2 import HelloWorld


class TestHelloWorld2(object):
    hw = None
    data = csv.reader(open("test_hello_world2.csv", mode="r", encoding="utf8"))

    @pytest.fixture(autouse=True)
    def prepare(self):
        """
        测试的固定装置
        :return:
        """
        self.hw = HelloWorld()
        print("prepare()")
        yield

        self.hw = None
        print("清理了对象 self.hw")

    def test_get_max_element(self):
        """
        类里面的单元测试
        :return:
        """
        print("test_get_max_element()")
        list_to_test = [2, 3, 99, 874, 44, -12]
        expected = 874
        actual = self.hw.get_max_element(list_to_test)
        assert expected == actual, "这次使用了类的 pytest"

    def test_get_max_element_02(self):
        """
        类里面的单元测试
        :return:
        """
        print("test_get_max_element_02()")
        list_to_test = [2, 3, 99, 874, 44, -12]
        expected = 874
        actual = self.hw.get_max_element(list_to_test)
        assert expected == actual, "这次使用了类的 pytest"

    def test_get_max_element_03(self):
        """
        类里面的单元测试
        :return:
        """
        print("test_get_max_element_03()")
        list_to_test = [2, 3, 99, 874, 44, -12]
        expected = 874
        actual = self.hw.get_max_element(list_to_test)
        assert expected == actual, "这次使用了类的 pytest"

    @pytest.mark.parametrize("csv_data", data)
    def test_add(self, csv_data):
        actual = self.hw.add(csv_data[0], csv_data[1])
        assert csv_data[2] == actual, "这次使用了类的 pytest参数化"
