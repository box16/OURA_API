from modules.calculator import Calculator
from modules.db_api import DBapi
from modules.grapher import Grapher

TABLE_NAMES = ["activity", "sleep", "readiness"]

ab_normal_column = [
    "hypnogram_5min",
    "hr_5min",
    "rmssd_5min",
    "class_5min",
    "met_1min", ]

skip_column = [
    "met_min_medium_plus",
    "bedtime_start",
    "bedtime_end"]

db_api = DBapi()
grapher = Grapher()
caluculator = Calculator()


def convert_abnormal_column_list(lists):
    result = []
    for _list in lists:
        if "," in _list:
            result.append([float(word) for word in _list.split(",")])
        else:
            result.append([float(word) for word in _list])
    return result


def cast_list_float(_list):
    return [float(value) for value in _list]


if __name__ == "__main__":
    data = {}
    # データ要素を取り出す
    for table in TABLE_NAMES:
        columns = db_api.get_column_names(table)
        for column in columns:
            _list = db_api.pick_column(table, column)
            if column in ab_normal_column:
                _list = convert_abnormal_column_list(_list)
                data[f"{column}_sum"] = caluculator.create_sum_list(_list)
                data[f"{column}_average"] = caluculator.create_average_list(
                    _list)
            elif column == "date":
                _list = [x.weekday() for x in _list]
                data["weekday"] = _list
            elif column in skip_column:
                pass
            else:
                _list = cast_list_float(_list)
                data[column] = _list

    keys = list(data.keys())
    combine_list = caluculator.create_combination_list(keys, 2)
    for combi in combine_list:
        try:
            grapher.scatter_plot_with_corrcoef(
                data[combi[0]], combi[0], data[combi[1]], combi[1])
        except BaseException:
            print(combi)
