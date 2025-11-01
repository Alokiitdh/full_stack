class Student:
    def __init__(self,name, rollno, m1,m2,m3,m4,m5):
        self.name : str = name
        self.rollno: int = rollno
        self.m1: float = m1
        self.m2: float = m2
        self.m3: float = m3
        self.m4: float = m4
        self.m5: float = m5

    @property
    def average(self):
        sum = self.m1 + self.m2 +self.m3 +self.m4 +self.m5
        avg= sum / 5
        return avg
    
    def __str__(self):
        return f"name = {self.name}, rollno = {self.rollno} and average is {self.average} "
stud1 = Student("Alice", 10001, 85, 90, 78, 92, 33)
stud2 = Student("Jack", 20001, 75, 80, 98, 42, 55)

print(stud1)
print(stud2)
