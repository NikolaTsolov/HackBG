import requests
import json
import sys
import sqlite3

class Request:
    def __init__(self):
        self.information = ""


    def get_information(self):
        r = requests.get("https://hackbulgaria.com/api/students/")
        return r.text



class DataBase:
    def __init__(self):
        self.db = sqlite3.connect('table.db')
        self.db.row_factory = sqlite3.Row
        self.table_query = self.db.cursor()
        self.table_query.execute("""PRAGMA foreign_keys = ON""")
        self.db.commit
        self.table_query.execute("""
        CREATE TABLE IF NOT EXISTS Students(
            student_id INTEGER PRIMARY KEY,
            name TEXT,
            github TEXT,
            available TEXT)""")
        self.table_query.execute("""
        CREATE TABLE IF NOT EXISTS Courses(
            course_id INTEGER PRIMARY KEY,
            name TEXT)""")
        self.db.commit
        self.table_query.execute("""
        CREATE TABLE IF NOT EXISTS Students_To_Courses(
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY(student_id) REFERENCES Students(student_id),
            FOREIGN KEY(course_id) REFERENCES Courses(course_id))""")
        self.db.commit
        self.r = Request()
        self.json_txt = self.r.get_information()

    def filling_the_db(self):
        into_json = json.loads(self.json_txt)
        courses_set = []
        for students in into_json:
            for courses in students["courses"]:
                courses_set.append(courses["name"])
            try:
                self.table_query.execute('''
                    INSERT INTO students(name, github,
                    available) VALUES(?,?,?)
                ''', (students["name"], students["github"], str(students["available"])))
            except:
                "We had errors"
            for course in courses_set:
                try:
                    print(course)
                    self.table_query.execute('''
                        INSERT INTO course(name) VALUES(?)
                    ''', (course, ))
                except:
                    "We had errors"
        print(set(courses_set))
        self.db.commit()

def main():
    d = DataBase()
    d.filling_the_db()



if __name__ == '__main__':
    main()
