#Create a new list from a two list using the following condition
#Given a two list of numbers, write a program to create a new list such that the new 
#list should contain odd numbers from the first list and even numbers from the second list.

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

resultingList = []
for num in list1:
    if num % 2 == 1:
        resultingList.append(num)
for num in list2:
    if num % 2 == 0:
        resultingList.append(num)

print(resultingList)