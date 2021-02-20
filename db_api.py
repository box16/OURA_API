import psycopg2
import os


class DBapi:
    def __init__(self):
        database_info = os.environ.get("OURADB")
        self._connection = psycopg2.connect(database_info)

    def add_activity(self, date, mets_1min):
        with self._connection.cursor() as cursor:
            if not self.check_dueto_insert(date):
                return
            cursor.execute(
                f"INSERT INTO activity (date,mets_1min) VALUES ('{date}','{mets_1min}');")
            self._connection.commit()

    def check_dueto_insert(self, date):
        with self._connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM activity WHERE date='{date}';")
            result = cursor.fetchall()
            if result:
                return False
            else:
                return True

    def pick_mets_1min(self, offset=None, limit=None):
        with self._connection.cursor() as cursor:
            q_offset = f" OFFSET {offset} " if offset else ""
            q_limit = f" LIMIT {limit} " if limit else ""
            query = "SELECT mets_1min FROM activity ORDER BY date" + q_offset + q_limit + ";"
            cursor.execute(query)
            return cursor.fetchone()[0]

    def count_column(self):
        with self._connection.cursor() as cursor:
            query = "SELECT count(date) FROM activity;"
            cursor.execute(query)
            return cursor.fetchone()[0]
