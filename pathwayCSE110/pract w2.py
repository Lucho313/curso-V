first_number = float(input("what is the first number? "))
second_number = float(input("what is the second number? "))

if first_number > second_number:
    print(f"The first number {first_number:.0f} is grater than the second number {second_number:.0f}")
elif first_number < second_number:
    print(f"The second number {second_number:.0f} is grater than the first number {first_number:.0f}")
elif first_number == second_number:
     print(f"Both numbers are equal: {first_number:.0f} = {second_number:.0f}")


print("")

animal = input("What is your favorite animal? ").lower()

if animal == "beart" or animal == "dog":
    print(f"The {animal} is my favorite animal too!")
elif animal :
    print(f"The {animal} is nice too but not my favorite.")
