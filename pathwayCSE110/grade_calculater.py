percentile = float(input("please provide the percentile: "))
is_passing_great = False
last_digit = percentile % 10

if percentile >= 90:
    grade = "A"
    is_passing_great = True
    if last_digit <3: 
        grade ="A-"
elif percentile >= 80:
    grade = "B"
    is_passing_great = True
    if last_digit >= 7:
        grade = "B+"
    elif last_digit <3: 
        grade ="B-"
elif percentile >= 70:
    grade = "C"
    is_passing_great = True
    if last_digit >= 7:
        grade = "C+"
    elif last_digit <3: 
        grade ="C-"
elif percentile >= 60:
    grade = "D"
    if last_digit >= 7:
        grade = "D+"
    elif last_digit <3: 
        grade ="D-"
else:
    grade = "F"

if is_passing_great:
    print("congratulations you are passing with a great grade!")
else:
    print("you are not passing but you can do better!")

print(f"your grade is {grade}")

