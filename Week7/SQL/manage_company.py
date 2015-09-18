import sqlite3

class ManageCompany:

    def __init__(self):
        self.db = sqlite3.connect(self.DB_NAME)
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
        list_employees = []
        self.table_query.execute("SELECT id,name,position FROM employees")
        for row in self.table_query:
            list_employees.append('{} - {} - {}'.format(row[0], row[1], row[2]))
        return list_employees

    def get_selary(self):
        monthly_selary = []
        self.table_query.execute("SELECT monthly_selary FROM employees")
        for row in self.table_query:
            monthly_selary.append(int(row[0]))
        return monthly_selary

    def get_yearly_bonus(self):
        yearly_bonus = []
        self.table_query.execute("SELECT yearly_bonus FROM employees")
        for row in self.table_query:
            yearly_bonus.append(int(row[0]))
        return yearly_bonus

    def add_employee(self, employee):
        self.table_query.execute('''
            INSERT INTO employees(name, monthly_selary,
            yearly_bonus, position) VALUES(?,?,?,?)
        ''', (employee[0], employee[1], employee[2], employee[3]))
        self.db.commit()

    def delete_employee(self, _id):
        self.table_query.execute('''
            DELETE FROM employees WHERE id = {}'''.format(_id))
        self.db.commit()

    def update_employee(self, employee, _id):
        self.table_query.execute('''
            UPDATE employees SET name = '{}', monthly_selary = {},
            yearly_bonus = {}, position = '{}' WHERE id = {}
            '''.format(employee[0], employee[1], employee[2], employee[3], _id))
        self.db.commit()

    DB_NAME = 'table.db'

if __name__ == '__main__':
    main()
