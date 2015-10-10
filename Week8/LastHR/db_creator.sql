DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Students_To_Courses;
PRAGMA foreign_keys = ON;

CREATE TABLE Students(
    student_id INTEGER PRIMARY KEY,
    student_name TEXT,
    github TEXT,
    available TEXT
);

CREATE TABLE Courses(
    course_id INTEGER PRIMARY KEY,
    course_name TEXT UNIQUE
);

CREATE TABLE Students_To_Courses(
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES Students(student_id),
    FOREIGN KEY(course_id) REFERENCES Courses(course_id)
);
