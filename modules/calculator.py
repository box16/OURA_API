import math
import copy

class Calculator:
    def __init__(self):
        pass

    def create_average_list(self, lists):
        result = copy.copy(lists[0])
        for _list in lists[1::]:
            for index, value in enumerate(_list):
                try:
                    result[index] += value
                except IndexError:
                    result.append(value)
        list_num = len(lists)
        return [value / list_num for value in result]

    def m_moving_result(self, _list, m):
        center_index = math.ceil(m / 2) - 1
        pick_num = math.floor((m - 1) / 2)
        result = []
        for index in range(center_index, len(_list) - center_index):
            _sum = sum([_list[pick] for pick in range(
                index - pick_num, index + pick_num + 1)])
            result.append(_sum / m)
        return result
