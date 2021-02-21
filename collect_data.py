from modules.oura_access import OuraAccess
from modules.db_api import DBapi
import datetime


def format_activity(activity):
    activity["met_1min"] = "'" + \
        ",".join([str(met) for met in activity["met_1min"]]) + "'"
    return activity


def format_sleep(sleep):
    sleep["hr_5min"] = "'" + ",".join([str(hr)
                                       for hr in sleep["hr_5min"]]) + "'"
    sleep["rmssd_5min"] = "'" + \
        ",".join([str(rm) for rm in sleep["rmssd_5min"]]) + "'"
    sleep["bedtime_start"] = f"'{sleep['bedtime_start'][11:19]}'"
    sleep["bedtime_end"] = f"'{sleep['bedtime_end'][11:19]}'"
    return sleep


def format_data(target, data):
    if target == "activity":
        return format_activity(data)
    elif target == "sleep":
        return format_sleep(data)
    return data


oura = OuraAccess()
db_api = DBapi()

for day_offset in range(1, 31):
    for target in ["activity", "sleep", "readiness"]:
        data = oura.collect_daily_summaries(target, day_offset)
        db_api.regist_data(target, data[0], format_data(target, data[1]))
    print(day_offset)
