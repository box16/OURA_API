import requests
import json
import os
import datetime
import collections
import pprint


class OuraAccess:
    def __init__(self):
        self._base_url = "https://api.ouraring.com/v1/"
        self._token = "access_token=" + str(os.environ.get("OURA_TOKEN"))

    def create_date_str(self, days_offset=0):
        today = datetime.datetime.today()
        target_date = today - datetime.timedelta(days=days_offset)
        return target_date.strftime("%Y-%m-%d")

    def create_url(self, date=None):
        if not date:
            raise ValueError("create_url date error!")
        url = f"{self._base_url}activity?start={date}&end={date}&{self._token}"
        return url

    def format_mets_1min(self, mets_1min):
        return ",".join([str(mets) for mets in mets_1min])

    def collect_activity(self, days_offset):
        headers = {"content-type": "application/json"}
        date_str = self.create_date_str(days_offset)
        api_url = self.create_url(date_str)
        responce = requests.get(api_url, headers=headers)
        data = responce.json()
        return data["activity"][0]
