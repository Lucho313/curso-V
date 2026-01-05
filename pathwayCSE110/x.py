"""""

grade = float(input("Enter your numeric grade: "))


penalty=  False
while grade <0 or grade > 100:

    print("invalid grade, please enter a grade correctly")
    print("you received a penalty of -5 points")
    penalty =True
    print ("")
    grade = float(input("enter your grade: "))
    grade = grade -5
    if penalty: True
    print(f"Your final grade after penalty is {grade}")

print(f"You got a {grade} grade!")


"""
"""
books = ["Book A", "Book B", "Book C", "Book D"]
books.pop(3) # removes "Book D"
books.insert(2, "Book F") # adds "Book F" at index 2
for i in range(len(books)):
    book = books[i]
    human_acounting = i +1
    print(f"{human_acounting} - {book}")

print("Please enter the items of the shopping list (type: 'quit' to finish):")
shopping_items = []
number_of_items = 0
A=True
while A :
    item = input("Item: ").lower()
    shopping_items.append(item)
    number_of_items += 1
    if item == "quit":
        break
    
print()
print("The shopping list is:")
print(f"there are {(number_of_items-1)} items in the list")
for i in shopping_items:
    print(i)
print()
while A :
    cuestion = input("Do you want to add items in the list (yes/no)? ").lower()
    if cuestion == "yes":
     index_in_item = input("Tell me the new item: ")
     shopping_items.append(index_in_item)
     number_of_items +=1
    else:
       print("Perfect so")
       break
print()
print("The shopping list is:")
print(f"there are {number_of_items} items in the list")
for i in shopping_items:
   # all_items = i
        break
for j in range(len(shopping_items)):
    #range_items= shopping_items[j]

        print(f"{j} - {i}")
        A=False
    
while True:
    cuestion = input("Do you want to delete items in the list (yes/no)? ").lower()
    print()
    if cuestion == "yes":
     index_in_item = int(input("Tell me the number of the item: "))
     shopping_items.pop(index_in_item)
     number_of_items -=1
    else:
       print("Perfect so")
       break
print()
print("The shopping list finish with these items:")
print(f"there are {number_of_items} items in the list")
for i in shopping_items:
   break

for j in range(len(shopping_items)):

        print(f"{j} - {i}")



#What is your message? The only thing we have to fear is FEAR itself!
#The only thing we have to fear is FEAR itself!
#HE ONLY THING WE HAVE TO FEAR IS FEAR ITSELF!
#the only thing we have to fear is fear itself!

def print_message_variations(user_message):
    print(user_message.lower()) 
    print(user_message.upper()) 
    print(user_message.capitalize())

print_message_variations(input("What is your message? "))

"""

def display_numbers(x, y):
    return 10

x = 3
y = 4
x = display_numbers(x, y)

print(x)