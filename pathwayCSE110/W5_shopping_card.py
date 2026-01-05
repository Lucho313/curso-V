"""""
Author: Luis Villegas

"""
# generar una lista de interaccion con el usuario. check
# empezar a desglozar las interacciones 'add', 'view total', 'remove', 'cerrar'. check
# finalizar interaccion con mostrando todo.check

"""Comments"""
# My creativity led me to do many things to make them more practical and special, such as asking if you would like to add more things to the list.
# I also think I do the program in a different way, but I really like the final result. 
# I feel that this time I was more professional in doing it.

opcion_menu = ["1. add item", "2. View cart","3. Remove item","4. Compute total","5. Quit"]
items_list = []
prices= []
total = 0
A= True
print()
print("Welcome to the Shopping Cart Program!")
print("Please enter the number to the left of the action to continue")
while A: 

    print("These are the actions available in your cart")
    for menu in opcion_menu:
        print(menu)
    
    choose = input("Please enter an action: ")
    if choose == "1" :
            items = input("What item would you like to add?: ")
            items_list.append(items)
            price = input(f"What is the price of {items}? ")
            prices.append(price)


            while A :
                cuestion = input("Do you want to add items in the cart (yes/no)? ").lower()
                if cuestion == "yes":
                    items= input("Tell me the new item: ")
                    items_list.append(items)
                    price = input(f"What is the price of {items}? ")
                    prices.append(price)
                    print(f"{items} has been added to the cart.")
                    for i in items_list:
                        break
                    for p in prices:
                        break
                else:
                    print("Perfect so")
                    print()
                    break
    elif choose == "2" :
         print("The shopping list is:")

         for i in range(len(items_list)):
              
              print(f"{i+1}. {items_list[i]} - ${prices[i]}")
            
    elif choose == "3" :
         print("The contents of the shopping cart are:")
         for i in range(len(items_list)):
              
              print(f"{i+1}. {items_list[i]} - ${prices[i]}")
            
         
         delete = int(input("Which item would you like to remove? ")) -1 
         items_list.pop(delete)
         prices.pop(delete)
         print("Item removed.")

    elif choose == "4":
     for p in prices:
         total += float(p)
    
     print(f"The total price of the items in the shopping cart is ${total:.2f}")
     print()
     total = 0
    elif choose == "5":
        print("Thank you. Goodbye.")
        A = False



    
        


