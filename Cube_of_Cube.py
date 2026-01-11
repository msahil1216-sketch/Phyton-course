#define function to calculate cube
def cube(number):
    return number*number*number 

#define a function which will execute cube function if the user entered a number divisble by 3
def by_three(number):
    if number %3 == 0:
        return cube(number)
    else:
        return False
#display result
print(by_three(18))
print(by_three(100))