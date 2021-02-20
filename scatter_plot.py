import matplotlib.pyplot as plt
import numpy
import os
import shutil
from db_api import DBapi

db_api = DBapi()
exclusion_list = {
    "sleep": [
        "bedtime_start",
        "bedtime_end",
        "hypnogram_5min",
        "hr_5min",
        "rmssd_5min"],
    "activity": [
        "class_5min",
        "met_1min"],
    "readiness": [],
}
target_table = "sleep"
target_column = "duration"
try:
    shutil.rmtree("figure")
except FileNotFoundError:
    pass
os.mkdir("figure")
objective = db_api.pick_column(target_table, target_column)


def create_graph(table, columns):
    for column in columns:
        if column in exclusion_list[table]:
            continue
        explanatory = db_api.pick_column(table, column)
        try:
            if numpy.corrcoef(explanatory, objective)[0][1] > 0.5:
                fig = plt.figure()
                plt.scatter(explanatory, objective)
                plt.ylabel(f"{target_table}:{target_column}")
                plt.xlabel(f"{table}:{column}")
                fig.savefig(
                    f"./figure/{target_table}:{target_column}-{table}:{column}.png")
                print(f"{column} create!")
        except BaseException:
            continue


if __name__ == "__main__":
    for table in ["activity", "sleep", "readiness"]:
        columns = db_api.get_column_names(table)
        create_graph(table, columns)
