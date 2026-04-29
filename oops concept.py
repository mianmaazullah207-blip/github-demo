#oops concept
class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display__inf(self):
            print("name", self.name)
            print("rollno:",self.rollno)
            print("marks:",self.marks)
    def result(self):
                if self.marks>50:
                    print("pass")
                else:
                    print("fail")
s1=Student("ali",67,85)
s1.display__inf()
s1.result()