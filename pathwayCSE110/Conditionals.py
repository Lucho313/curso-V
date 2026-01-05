temperature = float(input("what is your temperature in degrees celsius? "))
if temperature >= 40.5:
    print("Go to the hospital!")
elif temperature > 39.4:
    print("Call your doctor.")
else:
    print("Consider rest or medicine")

print("Have a good day")

"""
if (VARIABLE) >< : ## If the first condition is true, the program will execute the first block of code and skip the rest.
elif (VARIABLE) >< : ## If the first condition is false, but this condition is true, the program will execute this block of code and skip the rest.
else (VARIABLE) >< : ## If all previous conditions are false, the program will execute this block of code.

"""