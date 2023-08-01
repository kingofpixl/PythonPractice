#Given two integer numbers return their product only 
#if the product is equal to or lower than 1000, else return their sum.

def multOrSum(num1, num2):
    multiplication = number1 * number2
    addition = number1 + number2
    if multiplication <= 1000:
        return multiplication
    else:
        return addition

number1 = input('enter the first number: ')
number2 = input('enter the second number: ')

number1 = float(number1)
number2 = float(number2)

result = multOrSum(number1, number2)
print("the result is: ", result)

