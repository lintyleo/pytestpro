def get_max_element(alist: list):
    """
    获取最大的元素
    :param alist:
    :return:
    """
    max_value = alist[0]
    for value in alist:
        if max_value < value:
            max_value = value

    return max_value
