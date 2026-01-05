"""
Author: Luis Villegas

Purpose: Practice using lists, by adding the names of friends.
"""

print("Enter the name of your friends one by one. when you are done just type 'end'. ")
print()

friends = []
new_friend = ""
number_of_friends = 0

while new_friend != "end" :
    new_friend = input("Type the name of a friend: ").capitalize()
    if new_friend != "end":
        friends.append(new_friend)
        number_of_friends += 1

print()
print("your friends are:")
for friend in friends:
    print(friend)

print(f"Great you have {number_of_friends} friends!")



