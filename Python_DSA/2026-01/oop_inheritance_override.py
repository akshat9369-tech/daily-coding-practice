"""OOP: Inheritance, Method Overriding, and super()."""

class Employee:
    def __init__(self, name: str, emp_id: int, base_salary: float):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def calculate_pay(self) -> float:
        return self.base_salary

    def __str__(self) -> str:
        return f"Employee #{self.emp_id}: {self.name} | Pay: ${self.calculate_pay():.2f}"

class Manager(Employee):
    def __init__(self, name: str, emp_id: int, base_salary: float, bonus: float):
        super().__init__(name, emp_id, base_salary)
        self.bonus = bonus

    def calculate_pay(self) -> float:
        return super().calculate_pay() + self.bonus

if __name__ == "__main__":
    dev = Employee("Carlos", 101, 75000.0)
    mgr = Manager("Diana", 102, 95000.0, 15000.0)

    print(dev)
    print(mgr)
