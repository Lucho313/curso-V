
print("Hello and welcome to the meal price calculator!")
name = input("Please enter your name : ") 
Child_meal_price = float(input("Please enter the price of a Childs meal: "))
adult_meal_price = float(input("Please enter the price of an Adults meal: "))

print(f"Thank for that {name.capitalize()}!")

number_of_children = int(input("Please enter the number of children: "))
number_of_adults = int(input("Please enter the number of adults: "))

subtotal = (Child_meal_price * number_of_children) + (adult_meal_price * number_of_adults)
print(f"The subtotal is: ${subtotal:.2f}")
print()

sales_tax_rate = float(input("What is the sales tax rate? "))
sales_tax = subtotal * sales_tax_rate / 100
total = subtotal + sales_tax
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")
print()

Payment_amount = float(input("What is the payment amount? "))
change = Payment_amount - total
print(f"Change: ${change:.2f}")

