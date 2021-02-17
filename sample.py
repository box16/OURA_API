import requests
import json
import os
import datetime

BASE_URL = "https://api.ouraring.com/v1/"
API_LIST = ["userinfo","sleep","activity","readiness"]
TOKEN    = "access_token=" + str(os.environ.get("OURA_TOKEN"))

def create_date_str(weeks_offset=0):
    today = datetime.datetime.today()
    target_date = today - datetime.timedelta(days=1,
                                             weeks=weeks_offset)
    return target_date.strftime("%Y-%m-%d")

def create_url(weeks_offset=0):
    end_date = create_date_str(weeks_offset)
    start_date = create_date_str(weeks_offset+1)
    url = f"{BASE_URL}{API_LIST[2]}?start={start_date}&end={end_date}&{TOKEN}"
    return url

headers = {"content-type": "application/json"}
responce = requests.get(create_url(0), headers=headers)
data = responce.json()
for activity in data["activity"]:
    print(activity["score"])
