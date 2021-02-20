import psycopg2
import os


class DBapi:
    def __init__(self):
        database_info = os.environ.get("OURADB")
        self._connection = psycopg2.connect(database_info)

    def check_already_register(self, table, date):
        with self._connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {table} WHERE date='{date}';")
            result = cursor.fetchall()
            return result

    def regist_data(self, table, date, data):
        if self.check_already_register(table, date):
            self.update_table(table, date, data)
        else:
            self.insert_table(table, date, data)

    def update_table(self, table, date, data):
        with self._connection.cursor() as cursor:
            query = self.create_update_query(table, date, data)
            cursor.execute(query)
            self._connection.commit()

    def insert_table(self, table, date, data):
        with self._connection.cursor() as cursor:
            query = self.create_insert_query(table, date, data)
            cursor.execute(query)
            self._connection.commit()

    def create_update_query(self, table, date, data):
        column = ",".join(
            [key for key, value in sorted(data.items(), key=lambda x:x[0]) if key in self.get_column_names(table)])
        value = ",".join([str(value) for key, value in sorted(
            data.items(), key=lambda x:x[0]) if key in self.get_column_names(table)])
        return f"UPDATE {table} SET ({column}) = ({value}) WHERE date='{date}';"

    def create_insert_query(self, table, date, data):
        column = ",".join(
            [key for key, value in sorted(data.items(), key=lambda x:x[0]) if key in self.get_column_names(table)])
        value = ",".join([str(value) for key, value in sorted(
            data.items(), key=lambda x:x[0]) if key in self.get_column_names(table)])
        return f"INSERT INTO {table}(date,{column}) VALUES ('{date}',{value});"

    def get_column_names(self,table):
        with self._connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {table}")
            return [des[0] for des in cursor.description]


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
