

from dataclasses import dataclass
"""
We can define the datatypes in the class using the typehints annotation
self.name: str = name
"""
class Employee:

    COMPANY = "Google"

    def __init__(self, name, id, emailid, designation, phno, salary):
        self.id : int = id
        self.name: str = name
        self.emailid: str = emailid
        self.designation: str = designation
        self.phno: str = phno
        self.salary: float = salary

    def compare(self, other):
        if self.name == other.name:
            return True
        else:
            return False

emp1 = Employee(**{'name':'Alok',
                    'id': 117,
                     'emailid': 'aloklashok@gmailcom',
                      'designation':'AI Engineer',
                      'phno':'+91 7597694703',
                      'salary': 1200000})

emp2 = Employee(**{'name':'Alok V',
                    'id': 117,
                     'emailid': 'aloklashok@gmailcom',
                      'designation':'AI Engineer',
                      'phno':'+91 7597694703',
                      'salary': 1200000})

print(emp1.COMPANY)

result= emp1.compare(emp2)
print(result)



