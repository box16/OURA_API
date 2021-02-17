import requests
import json
import os
import datetime
import collections
import pprint

BASE_URL = "https://api.ouraring.com/v1/"
TOKEN    = "access_token=" + str(os.environ.get("OURA_TOKEN"))

def create_date_str(weeks_offset=0):
    today = datetime.datetime.today()
    target_date = today - datetime.timedelta(days=1,
                                             weeks=weeks_offset)
    return target_date.strftime("%Y-%m-%d")

def create_url(weeks_offset=0):
    end_date = create_date_str(weeks_offset)
    start_date = create_date_str(weeks_offset+1)
    url = f"{BASE_URL}activity?start={start_date}&end={end_date}&{TOKEN}"
    return url

if __name__ == "__main__":
    headers = {"content-type": "application/json"}
    mets_counter = collections.Counter()
    
    for week_offset in range(5):
        responce = requests.get(create_url(week_offset), headers=headers)
        data = responce.json()
        for activity in data["activity"]:
            mets_counter.update(activity["met_1min"])

    total_num = sum(mets_counter.values())
    for mets,count in mets_counter.items():
        mets_counter[mets] = count/total_num

    with open("mets.txt","w") as f:
        for mets,probability in mets_counter.items():
            f.write(f"{mets}\t{probability}\n")