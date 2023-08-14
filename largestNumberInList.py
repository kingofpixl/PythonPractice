numbers = [3, 6, 2, 8, 4, 10]
biggest = numbers[0]
for number in numbers:
    if number > biggest:
        biggest = number
print(f"Biggest number is: {biggest}")