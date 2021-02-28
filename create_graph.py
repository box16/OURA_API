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


def convert_column_list(column):
    if "," in column:
        return [float(word) for word in column.split(",")]
    else:
        return [float(word) for word in column]

def cast_list_float(_list):
    return [float(value) for value in _list]

def create_time_series_graph(table,column):
    try:
        ys = db_api.pick_column(table, column)
        ys = [convert_column_list(y) for y in ys]
        y_label = f"{table}:{column}"
        average_ys = caluculator.create_average_list(ys)
        grapher.line_graph(list(range(0,len(average_ys))), "time", average_ys, y_label)
    except TypeError:
        pass

def create_scatter_plot(y, y_label):
    for table in TABLE_NAMES:
        columns = db_api.get_column_names(table)
        for column in columns:
            if column in ab_normal_column:
                create_time_series_graph(table,column)
            else:
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
