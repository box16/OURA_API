import matplotlib.pyplot as plt
import os
import shutil
from db_api import DBapi

db_api = DBapi()
target_list = {
    "sleep": [
        "hypnogram_5min",
        "hr_5min",
        "rmssd_5min"],
    "activity": [
        "class_5min",
        "met_1min"],
    "readiness": [],
}
try:
    shutil.rmtree("figure")
except FileNotFoundError:
    pass
os.mkdir("figure")


def convert_column_list(column):
    if "," in column:
        return column.split(",")
    else:
        return [word for word in column]


def create_graph(_list, column):
    _list = [float(i) for i in _list]
    fig = plt.figure()
    plt.scatter(range(1, len(_list) + 1), _list)
    fig.savefig(
        f"./figure/{column}.png")
    print(f"{column} create!")


if __name__ == "__main__":
    for table, columns in target_list.items():
        for column in columns:
            pick = db_api.pick_column(table, column)
            _list = convert_column_list(pick[0])
            create_graph(_list, column)
