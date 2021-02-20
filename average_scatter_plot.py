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
        return [float(word) for word in column.split(",")]
    else:
        return [float(word) for word in column]


def create_graph(_list, column):
    fig = plt.figure()
    plt.scatter(range(1, len(_list) + 1), _list)
    fig.savefig(
        f"./figure/{column}.png")
    print(f"{column} create!")


def average_list(picks):
    result = convert_column_list(picks[0])
    picks_num = 0
    for pick in picks[1::]:
        picks_num += 1
        for index, value in enumerate(convert_column_list(pick)):
            try:
                result[index] += value
            except IndexError:
                result.append(value)
    return [value / picks_num for value in result]


if __name__ == "__main__":
    for table, columns in target_list.items():
        for column in columns:
            picks = db_api.pick_column(table, column)
            _list = average_list(picks)
            create_graph(_list, column)
