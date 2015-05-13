import sqlite3
class DataBase:
    def __init__(self):
        self.db = sqlite3.connect('table.db')
        self.db.row_factory = sqlite3.Row
        self.table_query = self.db.cursor()
        self.table_query.execute("""
        CREATE TABLE IF NOT EXISTS External_Links(
            student_id INTEGER PRIMARY KEY,
            name TEXT,
            github TEXT,
            available TEXT)""")
        self.db.commit
        self.r = Request()
        self.json_txt = self.r.get_information()

