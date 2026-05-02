class Student_Management_System:
    def __init__(self) -> None:
        self.top = {}
    def add_student(self, std_id, name, grade):
        if std_id not in self.top:
            self.top[std_id]={"ID":std_id, "Name":name, "Grade":grade}
        else:
            raise Exception("Fail to add student. ID already existed.")
    def update_grade(self, std_id, grade):
        self.top[std_id]["Grade"] = grade
    def display_all(self):
        print(*(v for k,v in self.top.items()))
if __name__ == "__main__":
    SMS = Student_Management_System()
    SMS.add_student(101,"Alice","A")
    SMS.display_all()
    SMS.update_grade(101,"A+")
    SMS.display_all()
    SMS.add_student(101,"Alice","A")
    SMS.display_all()
