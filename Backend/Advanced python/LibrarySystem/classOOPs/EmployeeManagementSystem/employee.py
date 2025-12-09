# Lets create a employee class
# emplyee is an object 

class Employee:
    def __init__(self, name, age, salary):
        self.name: str =name
        self.age: int = age
        self.salary: float = salary

    def get_info(self):
        return f"Employee Details \nName: {self.name} \nAge: {self.age} \nSalary: {self.salary}"

class EmployeeManager(Employee):
    def __init__(self):
        self.employees = []
        
    def add(self, name, age, salary ):
        emp = Employee(name, age, salary)
        self.employees.append(emp)
        print(f'Employee:{emp.name} added successfully')
        return self.employees
    
    def list_emp(self):
        for emp in self.employees:
            print(emp.get_info())
            print("-"*25)
        return f"Success"


manager = EmployeeManager()   

manager.add("Alok", 27, 20000)
manager.add("Ravi", 30, 30000)


print(manager.list_emp())

    