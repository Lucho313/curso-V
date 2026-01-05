"""""
Author: Luis Villegas.

numbers=[]
print()
print("Enter a list of numbers, type 0 when finished")
number_provided = int(input("Enter number: "))

while number_provided != 0 :
    numbers.append(number_provided)
    number_provided = int(input("Enter number: "))

sum = 0
for number in numbers :
    sum += number

highest = numbers[0]
for number in numbers :
    if highest < number :
        highest = number

average = sum/len(numbers)

smallest_positive = highest
for number in numbers:
    if number > 0:
       if smallest_positive > number:
           smallest_positive = number

print(f"The sum is: {sum}")
print(f"The average is: {average}")
print(f"The largest number is: {highest}")
print(f"The smallest positive number is: {smallest_positive}")

"""

numbers = [1, 2, 3]
for animal in numbers:
    print(animal)