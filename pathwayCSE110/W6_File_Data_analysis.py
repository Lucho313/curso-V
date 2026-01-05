
# Author : Luis David Villegas Robles.
# My creativity gave me a way to save all the data for reuse with names like lowest and maximum, thus keeping it short

lowest_life = 999999999
max_life = 0

user_year= int(input("Enter the year of interest: "))

year_life_sum = 0 
year_life_acount = 0
year_max= -1
year_max_country=""
year_min = 99999999
year_min_country=""


with open("life-expectancy.csv") as document:
    next(document)

    for line in document:

        parts = line.split(",")
        countrys = parts[0]
        code = parts[1]
        years = int(parts[2])
        lives = float(parts[3])
        
        if lives < lowest_life:
            lowest_life = lives
            lowest_country= countrys
            lowest_year= years
        if lives > max_life:
           max_life = lives
           max_country= countrys
           max_year= years


        if years == user_year:
            year_life_sum += lives
            year_life_acount += 1

            if lives > year_max:
                year_max = lives
                year_max_country = countrys
            
            if lives < year_min:
                year_min = lives
                year_min_country = countrys

year_average = year_life_sum/year_life_acount

print(f"The overall max life expectancy is: {max_life} from {max_country} in {max_year}")
print(f"The overall min life expectancy is:: {lowest_life} from {lowest_country} in {lowest_year}")
print()
print(f"For the year {user_year}:")
print(f"The average life expectancy across all countries was {year_average:.2f}")
print(f"The max life expectancy was in {year_max_country} with {year_max}")
print(f"The min life expectancy was in {year_min_country} with {year_min}")