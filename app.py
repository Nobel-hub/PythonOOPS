class Employee:
    def __init__(self, name, id, department, salary, designation):
        self.name = name
        self.id = id
        self.department = department
        self.salary = salary
        self.designation = designation
    def report(self):
        return f"Employee Name: {self.name}, ID: {self.id}, Department: {self.department}, Salary: {self.salary}, Designation: {self.designation}"
    def presentation(self):
        return f"{self.name} is presenting a report on {self.department} department."
    def travel(self, destination):
        return f"{self.name} is traveling to {destination} for a business meeting."


if __name__ == "__main__":
    emp1 = Employee("Alice", 101, "HR", 50000, "Manager")
    emp2 = Employee("Bob", 102, "IT", 60000, "Developer")
    
    print(emp1.report())
    print(emp2.report())
    
    print(emp1.presentation())
    print(emp2.presentation())
    
    print(emp1.travel("New York"))
    print(emp2.travel("San Francisco"))