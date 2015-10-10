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
        self.conn = sqlite3.connect('hr.db')
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        creator = self.file_reader("db_creator.sql")
        self.cursor.executescript(creator)
        self.conn.commit
        self.json_txt = self.file_reader("new_hr.txt")

    ADD_STUDENTS = """
        INSERT INTO Students(student_name, github, available)
        VALUES(?, ?, ?)
    """

    ADD_COURSE = """
        INSERT INTO Courses(course_name)
        VALUES(?)
    """

    STUDENT_COURSES = """
        INSERT INTO Students_To_Courses(student_id, course_id)
        VALUES(?, ?)
    """

    GET_COURSE_ID = """
        SELECT course_id
        FROM Courses
        WHERE course_name = ?
    """

    GET_STUDENT_ID = """
        SELECT student_id
        FROM Students
        WHERE student_name = ?
    """

    GET_STUDENTS = """
        SELECT student_name, github
        FROM Students
    """

    GET_COURSES = """
        SELECT course_name
        FROM Courses
    """

    COURSES_ATTENDED = """
        SELECT s.student_name, c.course_name
        FROM Students s
        JOIN Students_To_Courses s_c
        ON s_c.student_id = s.student_id
        JOIN Courses c
        ON c.course_id = s_c.course_id
    """

    MOST_ATTENDED = """
        SELECT s.student_id, s.student_name, COUNT(s_c.course_id) AS cours_count
        FROM Students s
        LEFT JOIN Students_To_Courses s_c
        ON s.student_id = s_c.student_id
        WHERE s.student_id = ?
    """

    COUN_S_ID = """
        SELECT COUNT(student_id)
        FROM Students
    """

    def get_course_id(self, name):
        try:

            self.cursor.execute(self.GET_COURSE_ID, (name, ))
            for row in self.cursor:
                c_id = row[0]
            return c_id
        except:
            print("HaHa")

    def get_student_id(self, name):
        try:
            self.cursor.execute(self.GET_STUDENT_ID, (name, ))
            for row in self.cursor:
                s_id = row[0]
            return s_id
        except:
            print("Errorr")

    @staticmethod
    def file_reader(f_name):
        with open(f_name, "r") as f:
            return f.read()

    def filling_the_db(self):
        into_json = json.loads(self.json_txt)
        for students in into_json:
            try:
                self.cursor.execute(self.ADD_STUDENTS, (students["name"], students["github"], str(students["available"])))
            except:
                print("We had errors")
            for course in students["courses"]:
                try:
                    self.cursor.execute(self.ADD_COURSE, (course["name"], ))
                except:
                    pass
                c_id = self.get_course_id(course["name"])
                s_id = self.get_student_id(students["name"])
                self.cursor.execute(self.STUDENT_COURSES, (s_id, c_id))
        self.conn.commit()

    def get_students(self):
        self.cursor.execute(self.GET_STUDENTS)
        for row in self.cursor:
            print("{} : {}".format(row[0], row[1]))

    def get_courses(self):
        self.cursor.execute(self.GET_COURSES)
        for row in self.cursor:
            print("{}".format(row[0]))

    def courses_attended(self):
        self.cursor.execute(self.COURSES_ATTENDED)
        for row in self.cursor:
            print("{} : {}".format(row[0], row[1]))

    def most_attended(self):
        count = self.cursor.execute(self.COUN_S_ID).fetchone()
        max_courses = 0
        students = []
        for s_id in range(1, count[0] + 1):
            row = self.cursor.execute(self.MOST_ATTENDED, (s_id, )).fetchone()
            if row[2] > max_courses:
                max_courses = row[2]
                students = []
                students.append(row[1])
            elif row[2] == max_courses:
                students.append(row[1])
        print(students)


def main():
    d = DataBase()
    d.filling_the_db()
    d.get_students()
    d.get_courses()
    d.courses_attended()
    d.most_attended()






if __name__ == '__main__':
    main()
