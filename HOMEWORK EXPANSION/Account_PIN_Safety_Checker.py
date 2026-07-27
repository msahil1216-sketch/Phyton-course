class Account:

    def __init__(self, name, pin):
        self.name = name
        self.__pin = pin    

    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN Updated Successfully!")
        else:
            print("Invalid PIN! PIN must contain exactly 4 digits.")

    def get_pin(self):
        return self.__pin

    def __str__(self):
        return f"Account Holder: {self.name}\nPIN: ****"


account1 = Account("Muhammad", "1234")

print(account1)

print("Current PIN:", account1.get_pin())

account1.set_pin("5678")

print("Updated PIN:", account1.get_pin())