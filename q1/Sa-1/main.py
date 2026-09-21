class AssignmentSubmission:
    def __init__(
        self,
        student_name,
        student_id,
        assignment_title,
        due_date,
        is_submitted: bool = False,
        grade: float = 0.0,
        submitted_files: list[str] | None = None,
    ):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = is_submitted
        self.__grade = grade
        self.__submitted_files = submitted_files if submitted_files is not None else []

    def __validate_grade(self, score: float) -> bool:
        return 0 <= score <= 100

    def __check_submission_status(self) -> bool:
        return self.__is_submitted

    def __is_duplicate(self, file_name: str) -> bool:
        return file_name in self.__submitted_files

    def add_file(self, file_name: str):
        if self.__is_duplicate(file_name):
            print(f"[Warning] {file_name} is already attached!")
        else:
            self.__submitted_files.append(file_name)
            print("[Success]", self.student_name, "attached", file_name, ". Total files:", len(self.__submitted_files))

    def remove_file(self, file_name: str):
        if self.__grade > 0:
            print("[Warning]", self.student_name, "cannot remove files. Assignment already graded.")
            return
        elif file_name in self.__submitted_files:
            self.__submitted_files.remove(file_name)
            print("[Success]", self.student_name, "removed", file_name, ". Total files:", len(self.__submitted_files))
        


    def assign_grade(self, score: float):
        if not self.__validate_grade(score):
            print("Invalid grade. Please enter a grade between 0 and 100.")
            return
        if len(self.__submitted_files) == 0:
            print("[Error] Cannot grade. No files submitted for.", self.student_name)
            return

        self.__grade = score
        self.__is_submitted = True
        print("[Success] Grade", self.__grade, "officially assigned to", self.student_name)

    def get_grade(self):
        return self.__grade

    def view_files(self):
        return self.__submitted_files

    def get_status_report(self):
        return {
            "ID:": self.student_id,
            "Name:": self.student_name,
            "Status:": "Submitted" if len(self.__submitted_files) > 0 else "Missing",
            "Grade:": self.__grade if self.__grade > 0 else "Not Graded",
        }


student1 = AssignmentSubmission("Alex Gonzaga", "pshs-1090-x", "CS-101", "2026-10-01")
student2 = AssignmentSubmission("Adelle", "pshs-1920-x", "CS-103", "2026-10-01")
student3 = AssignmentSubmission("Juan dela Cruz", "pshs-1033-x", "CS-101", "2026-10-01")
student4 = AssignmentSubmission("Maria Santos", "pshs-1044-x", "CS-101", "2026-10-01")
student5 = AssignmentSubmission("Jose Reyes", "pshs-1055-x", "CS-101", "2026-10-01")

print("--- TEST SCENARIO 1: Multiple Files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("--- TEST SCENARIO 2: Removing Files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.docx")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")
student3.add_file("script.py")
student3.add_file("script.py")
print(f"Juan's Files: {student3.view_files()}\n")

print("--- TEST SCENARIO 4: Removing file after being graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf")
print()

print("--- TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100)
print()

print("--- FINAL SYSTEM REPORT ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())