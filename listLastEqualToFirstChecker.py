#Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def firstEqualLast(list):
    print('Given the list: ', list)
    if list[0] == list[-1]:
        return True
    else:
        return False

print('The result is ', firstEqualLast(numbers_x))
print('The result is ', firstEqualLast(numbers_y))
