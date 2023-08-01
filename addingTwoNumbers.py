
#program that add 2 numbers

#variables dont need to be declared as python is dynamic with their variable types
#python doesnt need ; like c++
#input will also ask the question and take the input as a string
number1 = input('enter the first number: ')
number2 = input('enter the second number: ')

#input returns a string and thus we use float() to change it to a float

addition = float(number1) + float(number2)

#print outputs to the user, the .format part makes it so the {0}, {1}, and {2} 
#work by formating the parameters to the correct spot

print('the sum of {0} and {1} = {2}'.format(number1, number2, addition))