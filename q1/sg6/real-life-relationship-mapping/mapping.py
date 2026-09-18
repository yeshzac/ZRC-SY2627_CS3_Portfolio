class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def __repr__(self):
        return f"Student(id={self.student_id}, name='{self.name}')"

class Course:
    def __init__(self, course_id, title):
        self.course_id = course_id
        self.title = title
        self.students = []
