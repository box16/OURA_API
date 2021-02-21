from modules.calculator import Calculator
from modules.db_api import DBapi
from modules.grapher import Grapher

TABLE_NAMES = ["activity", "sleep", "readiness"]

ab_normal_column = [
    "hypnogram_5min",
    "hr_5min",
    "rmssd_5min",
    "class_5min",
    "met_1min",
    "date",
    "met_min_medium_plus",
    "bedtime_start",
    "bedtime_end"]

db_api = DBapi()
grapher = Grapher()
caluculator = Calculator()

# そのままでは扱えないデータを整形する

# 平均値のグラフを描く

# 移動平均のグラフを描く


def cast_list_float(_list):
    return [float(value) for value in _list]


def create_scatter_plot(y, y_label):
    for table in TABLE_NAMES:
        columns = db_api.get_column_names(table)
        for column in columns:
            if column in ab_normal_column:
                continue
            x = db_api.pick_column(table, column)
            x = cast_list_float(x)
            x_label = f"{table}:{column}"
            grapher.scatter_plot_with_corrcoef(x, x_label, y, y_label)


if __name__ == "__main__":
    target_table = "sleep"
    target_column = "total"
    y = db_api.pick_column(target_table, target_column)
    y = cast_list_float(y)
    y_label = f"{target_table}:{target_column}"
    create_scatter_plot(y, y_label)
