class Employee:
    def __init__(self, name, number, department):
        self.__name = name
        self.__number = number
        self.__department = department

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def set_department(self, department):
        self.__department = department

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    def get_department(self):
        return self.__department

class ProductionWorker(Employee):
    def __init__(self, name, number, department, pay_rate, shift, discount_rate):
        super().__init__(name, number, department)
        self.__pay_rate = pay_rate
        self.__shift = shift
        self.__discount_rate = discount_rate

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def set_shift(self, shift):
        self.__shift = shift

    def set_discount_rate(self, discount_rate):
        self.__discount_rate = discount_rate

    def get_pay_rate(self):
        return self.__pay_rate

    def get_shift(self):
        return self.__shift

    def get_discount_rate(self):
        return self.__discount_rate

def parse_shift(shift_input):
    word_to_num = {
        "one": 1,
        "two": 2,
        "three": 3,
        "1": 1,
        "2": 2,
        "3": 3
    }
    return word_to_num.get(shift_input.lower(), None)

# Program to demonstrate the ProductionWorker class
if __name__ == "__main__":
    # Prompt the user for input
    name = input("Enter employee name: ")
    number = input("Enter employee number: ")
    department = input("Enter employee department (e.g., Manufacturing, Engineering, HR): ")
    
    while True:
        try:
            pay_rate = float(input("Enter hourly pay rate: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for the pay rate.")

    while True:
        shift_input = input("Enter shift number (1 for day, 2 for night) or as word (one, two): ")
        shift = parse_shift(shift_input)
        if shift in [1, 2]:
            break
        else:
            print("Invalid input. Please enter '1' or '2', or 'one' or 'two'.")

    while True:
        try:
            discount_rate = float(input("Enter employee discount rate (as a percentage, e.g., 10 for 10%): "))
            if 0 <= discount_rate <= 100:
                break
            else:
                print("Invalid input. Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the discount rate.")

    # Create an instance of ProductionWorker
    worker = ProductionWorker(name, number, department, pay_rate, shift, discount_rate)

    # Display the data
    print("\nTesla Employee Information:")
    print(f"Name: {worker.get_name()}")
    print(f"Number: {worker.get_number()}")
    print(f"Department: {worker.get_department()}")
    print(f"Hourly Pay Rate: ${worker.get_pay_rate():.2f}")
    print(f"Shift: {'Day' if worker.get_shift() == 1 else 'Night'}")
    print(f"Employee Discount Rate: {worker.get_discount_rate():.2f}%")
