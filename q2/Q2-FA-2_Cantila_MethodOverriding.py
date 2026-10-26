class Patient:
    def __init__ (self, name: str, bill_amount: float):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.get_bill_amount()

class Senior_Patient(Patient):
    def __init__(self, name: str, bill_amount: float, discount_rate: float):
        super().__init__(name, bill_amount)
        self.__discount_rate = 0.20

    def calculate_bill(self):
        original_bill = super().calculate_bill()
        discount_amount = original_bill * self.__discount_rate
        return original_bill - discount_amount

class PhilHealth_Patient(Patient):
    def __init__(self, name: str, bill_amount: float, discount_rate: float):
        super().__init__(name, bill_amount)
        self.__discount_rate = 0.15

    def calculate_bill(self):
        original_bill = super().calculate_bill()
        discount_amount = original_bill * self.__discount_rate
        return original_bill - discount_amount

print("Hospital Billing System")
print("-------------------------")
Patient1 = Patient("Juan Dela Cruz", 15000.00)
Patient2 = Senior_Patient("Maria Santos", 15000.00, 0.20)
Patient3 = PhilHealth_Patient("Pedro Reyes", 15000.00, 0.15)

print(f"Patient Name: {Patient1.get_name()}")
print(f"Original Bill: {Patient1.get_bill_amount()}")
print(f"Final Bill: {Patient1.calculate_bill()}")

print(f"\nPatient Name: {Patient2.get_name()}")
print(f"Original Bill: {Patient2.get_bill_amount()}")
print(f"Final Bill: {Patient2.calculate_bill()}")

print(f"\nPatient Name: {Patient3.get_name()}")
print(f"Original Bill: {Patient3.get_bill_amount()}")
print(f"Final Bill: {Patient3.calculate_bill()}")
