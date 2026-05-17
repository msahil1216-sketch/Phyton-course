# Create Class
class Employee:

    # Initializing
    def __init__(self):
        print("Employee created")

    # Calling destructor
    def __del__(self):
        print("Destructor called")

def Create_obj():
    print('Making Objects...')
    obj = Employee()
    print('funtion end...')
    return obj

print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')