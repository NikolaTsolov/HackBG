import sqlite3

class TableCreator:
    def __init__(self, database):
        self.db = sqlite3.connect('table.db')
        self.db.row_factory = sqlite3.Row
        self.table_query = self.db.cursor()
        self.table_query.execute("""
        CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY,
            name TEXT,
            monthly_selary INTEGER,
            yearly_bonus INTEGER,
            position TEXT)""")
        self.db.commit

    def create_company(self):
        names = ['Ivan Ivanov', 'Rado Rado', 'Ivo Ivo', 'Petar Petrov', 'Maria Georgieva']
        monthly_selary = [5000, 500, 10000, 3000, 8000]
        yearly_bonus = [10000, 0, 100000, 1000, 10000]
        position = ['Software Developer', 'Technical Support Intern', 'CEO', 'Marketing Manager', 'COO']
        for i in range(0, len(names)):
            try:
                self.table_query.execute('''
                    INSERT INTO employees(name, monthly_selary,
                    yearly_bonus, position) VALUES(?,?,?,?)
                ''', (names[i], monthly_selary[i], yearly_bonus[i], position[i]))
            except:
                "We had errors"
            self.db.commit()

    def list_employees(self):
        #self.table_query.execute("DELETE FROM employees WHERE id = 1 OR 1 = 1")
        self.table_query.execute("SELECT id,name,position FROM employees")
        for row in self.table_query:
            print('{0} - {1} - {2}'.format(row.id, row.name, row.position))

def main():
    db = TableCreator()
    db.list_employees()


if __name__ == '__main__':
    main()
