import requests
import json
import os
import datetime
import collections
import pprint
from db_access import DBAccess

BASE_URL = "https://api.ouraring.com/v1/"
TOKEN    = "access_token=" + str(os.environ.get("OURA_TOKEN"))

def create_date_str(days_offset=0):
    today = datetime.datetime.today()
    target_date = today - datetime.timedelta(days=days_offset)
    return target_date.strftime("%Y-%m-%d")

def create_url(days_offset=0):
    end_date = create_date_str(days_offset)
    start_date = create_date_str(days_offset+1)
    url = f"{BASE_URL}activity?start={start_date}&end={end_date}&{TOKEN}"
    return url

def format_mets_1min(mets_1min):
    return ",".join([str(mets) for mets in mets_1min])

if __name__ == "__main__":
    db_access = DBAccess()
    headers = {"content-type": "application/json"}
    for days_offset in range(0,30):
        responce = requests.get(create_url(days_offset), headers=headers)
        data = responce.json()
        day_text = create_date_str(days_offset)
        mets_text = format_mets_1min(data["activity"][0]["met_1min"])
        db_access.add_activity(day_text,mets_text)

