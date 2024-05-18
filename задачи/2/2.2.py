class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.subjects = {}

    def add_subject(self, subject, grade):
        self.subjects[subject] = grade
    
    def remove_subject(self, subject):
        if subject in self.subjects:
            del self.subjects[subject]
    
    def average_grade(self):
        if not self.subjects:
            return 0
        return sum(self.subjects.values()) / len(self.subjects)


student = Student("Ivan", 20)
student.add_subject("Math", 90)
student.add_subject("Physics", 85)
student.remove_subject("Math")
print(student.average_grade())  
