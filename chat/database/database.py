import config as Config
import mysql.connector as con


class CursorByName():
    def __init__(self, cursor):
        self._cursor = cursor

    def __iter__(self):
        return self

    def __next__(self):
        row = self._cursor.__next__()
        return {description[0]: row[col] for col, description in enumerate(self._cursor.description)}


class DataBase():
    def __init__(self, connector) -> None:
        self.connector = connector
        self.config = Config.Config()
        self.con = self.get_conector()
        self.cursor = self.con.cursor()

    def get_conector(self):
        if self.connector == "mysql.connector":
            return con.connect(
                host=self.config.server,
                user=self.config.user,
                passwd=self.config.password,
                database=self.config.dbname,
                port=self.config.port
            )

    def get_all(self, table):
        self.cursor.execute(f"SELECT * FROM {table}")
        return CursorByName(self.cursor)

    def get_columns(self, table):
        self.cursor.execute(f"SELECT * FROM {table}")
        return self.cursor.column_names
