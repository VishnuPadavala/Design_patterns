from student import student
class studentbuilder:
    def __init__(self):
        self.student=student()
    def set_name(self,name):
        self.student.name=name
        return self
    def set_rollno(self,rollno):
        self.student.rollno=rollno
        return self
    def set_phoneno(self,phoneno):
        self.student.phoneno=phoneno
        return self
    def build(self):
        return self.student