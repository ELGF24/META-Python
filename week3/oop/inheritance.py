class Employee:

    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last

class Supervisor(Employee):

    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password

class Chef(Employee):
    # def __init__(self, name, last) -> None:
    #     super().__init__(name, last)

    def leave_request(self, days):
        return f"May I take a leave for {days} days"

a = Employee("Erik", "glez")
b = Supervisor("Erik", "glez", 123)
c = Chef("Erik", "glez")

print(b.password)
print(c.leave_request(3))