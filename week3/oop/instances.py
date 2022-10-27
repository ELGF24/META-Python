class PayList:

    def __init__(self, name, payment, amount):
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = True

    def status(self):
        if self.payment:
            return f"{self.name} is paid, {self.amount}"
        else:
            return f"{self.name} is not paid yet"

nathan = PayList("nathan", True, 403)
carlos = PayList("carlos", True, 504)
david = PayList("david", False, 350)

print(nathan.status())
print(carlos.status())
print(david.status())

david.pay()
print(david.status())