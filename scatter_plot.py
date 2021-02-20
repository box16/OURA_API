import matplotlib.pyplot as plt
import numpy
import os
import shutil
from db_api import DBapi
import traceback
import re

db_api = DBapi()
exclusion_list = {
    "sleep": [
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


def scatter(explanatory, objective, table, column):
    fig = plt.figure()
    plt.scatter(explanatory, objective)
    plt.ylabel(f"{target_table}:{target_column}")
    plt.xlabel(f"{table}:{column}")
    fig.savefig(
        f"./figure/{target_table}:{target_column}-{table}:{column}.png")
    print(f"{column} create!")


def create_graph(table, columns):
    for column in columns:
        if column in exclusion_list[table]:
            continue
        explanatory = db_api.pick_column(table, column)
        try:
            if numpy.corrcoef(explanatory, objective)[0][1] > 0.5:
                scatter(explanatory, objective, table, column)
        except TypeError:
            if None in explanatory:
                continue
            explanatory = [int(re.sub(r"-|:", "", str(e)))
                           for e in explanatory]
            if numpy.corrcoef(explanatory, objective)[0][1] > 0.5:
                scatter(explanatory, objective, table, column)


if __name__ == "__main__":
    for table in ["activity", "sleep", "readiness"]:
        columns = db_api.get_column_names(table)
        create_graph(table, columns)
