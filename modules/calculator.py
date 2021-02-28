import math
import copy


class Calculator:
    def __init__(self):
        pass

    def create_average_list(self, lists):
        """リストのリストを渡して、平均値のリストを返す\n
            in :[[1,2,3],[4,5,6]]
            out : [2.5,3.5,4.5]
        """
        result = copy.copy(lists[0])
        for _list in lists[1::]:
            for index, value in enumerate(_list):
                try:
                    result[index] += value
                except IndexError:
                    result.append(value)
        list_num = len(lists)
        return [value / list_num for value in result]

    def m_moving_average(self, _list, m):
        """m項移動平均を計算する\n
            in : [1,2,3,4,5,6,7,8,9] , 3
            out : [2.0,3.0,4.0,5.0,6.0,8.0]
            in : [1,2,3,4,5,6,7,8,9] , 4
            out : [3.0,4.0,5.0,6.0]
        """
        if m % 2 == 0:
            center_index = math.ceil(m / 2)
            pick_num = math.floor((m - 1) / 2)
            result = []
            for index in range(center_index, len(_list) - center_index):
                _sum = sum([_list[pick] for pick in range(index - pick_num,
                                                          index + pick_num + 1)] + [_list[index - pick_num - 1] / 2,
                                                                                    _list[index + pick_num + 1] / 2])
                result.append(_sum / m)
        else:
            center_index = math.ceil(m / 2) - 1
            pick_num = math.floor((m - 1) / 2)
            result = []
            for index in range(center_index, len(_list) - center_index):
                _sum = sum([_list[pick] for pick in range(
                    index - pick_num, index + pick_num + 1)])
                result.append(_sum / m)
        return result
