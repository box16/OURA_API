import psycopg2
import os

class DBAccess:
    def __init__(self):
        database_info = os.environ.get("OURADB")
        self._connection = psycopg2.connect(database_info)
    
    def add_activity(self,date,mets_1min):
        with self._connection.cursor() as cursor:
            if not self.check_dueto_insert_activity(date):
                return
            cursor.execute(
                f"INSERT INTO activity (date,mets_1min) VALUES ('{date}','{mets_1min}');")
            self._connection.commit()
    
    def check_dueto_insert_activity(self, date):
        with self._connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM activity WHERE date='{date}';")
            result = cursor.fetchall()
            if result:
                return False
            else:
                return True