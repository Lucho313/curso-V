"""""
Author : Luis David Villegas Robles 
Date : Nov 14, 2025

"""""
#I really enjoyed this activity. My dream is to make video games, and I've always loved these interactive story games. Well,
# you could say this is the first time I've made one.

#I think I demonstrate my creativity in everything, starting with asking "are you ready?" 
# and also including an "else:" with a funny message to prevent other scenarios.

# I showed this to two friends who are also more experienced programmers, and they
# laughed when they saw the endings and also helped me a little to correct errors, but more than a laugh, it made us laugh. 

print("Zombie Survival Story")
print("")
print("Try to survive. The options will appear in capital letters as (EXAMPLE).")
print("")
input("Ready? ")

print("Start…")
print("")
print("You wake up alone in a forest in the early morning. Not far away "
       "you see a cabin to the south, and to the north, a road leading to a bridge that takes you to a nearby city…")

desciption_1 = input("You get up and must decide whether to go to the CABIN or the CITY or RUN through the forest. Where will you go?:  ").upper()

# Cabin scenario

if desciption_1 == "CABIN":
    print("")
    print("Once you're standing, you approach the cabin…")
    bag_option = input("At the entrance, you see a bag next to the door… Do you want to check the bag?... YES or NO : ").upper()
    if bag_option == "YES":
        print("")
        desciption_1_2 = input("Great, you got a rusty weapon... You're standing in front of the cabin door and you hear a strange noise not far away..." 
        " You have two options to go INSIDE the cabin or to INVESTIGATE the noise. What will you do? : ").upper()
    
        if desciption_1_2 == "INSIDE":
            print("")
            print("You rush into the cabin and as you close the door, you are struck by something unknown and devoured by zombies…. THE END")
        elif desciption_1_2 == "INVESTIGATE":
            print("")
            print("As you approach stealthily through the trees, you encounter some zombies… when you turn around, you see that you are surrounded…" 
            " you draw your weapon, but it jams when you try to fire, and you are tragically bitten and turned into a zombie")
        else:
            print("")
            print("You hadn't even decided what to do and a zombie dog ate you... THE END")
            print("Try again using the correct options marked in capital letters (EXAMPLE).")
    elif bag_option == "NO": 
         print("")
         desciption_1_2 = input("You're standing in front of the cabin door and you hear a strange noise not far away..." 
         " You have two options to go INSIDE the cabin or to INVESTIGATE the noise. What will you do? : ").upper()
         if desciption_1_2 == "INSIDE":
            print("")
            print("You rush into the cabin and as you close the door, you are struck by something unknown and devoured by zombies…. THE END")
         elif desciption_1_2 == "INVESTIGATE":
            print("")
            print("As you approach stealthily through the trees, you encounter some zombies… when you turn around, you see that you are surrounded…" 
            " and you are tragically bitten and turned into a zombie")

         else:
          print("")
          print("You hadn't even decided what to do and a zombie dog ate you... THE END")
          print("Try again using the correct options marked in capital letters (EXAMPLE).")

    else:
        print("")
        print("You hadn't even decided what to do and a zombie dog ate you... THE END")
        print("Try again using the correct options marked in capital letters (EXAMPLE).")
else:
    pass

if desciption_1 == "RUN" or desciption_1 == "RUN THROUGH THE FOREST":
    print("")
    print("You ran into the forest and got lost, after hours of wandering you were surrounded by zombies and bitten... THE END")

# city scenario

if desciption_1 == "CITY":
    print("")
    print("You walk calmly in that direction, and the path seems deserted…")
    desciption_1_2 = input("When you're near the bridge, you notice zombies nearby who haven't noticed you yet. You panic and must quickly choose between RUNNING or CALMING DOWN and continuing to walk. What will you do? : ").upper()
    if desciption_1_2 == "RUNNING" or desciption_1_2 == "RUN":
        print("")
        print("You start running and the zombies around you notice, they chase you, and halfway across the bridge you trip and a zombie quickly bites you. You manage to escape and at the end of the bridge," 
        " not far away, you see a person who doesn't appear to be a zombie.")
        desciption_1_3 = input("You have two options: TALK to the person or TURN AROUND and continue on your way through the city. What will you do? : ").upper()
        if desciption_1_3 == "TALK":
            print("")
            print("You approach and, upon speaking with the person, she tells you her name is Darling and that she's a survivor, that there are more like her. But she notices you've been bitten, quickly pulls out her weapon, and shoots you. You die staring at the morning sky… THE END")
        elif desciption_1_3 == "TURN AROUND" or desciption_1_3 == "TURN" or desciption_1_3 == "AROUND":
            print("")
            print("You wandered around all day feeling the pain of the bite, and by the end of the afternoon, you were just another zombie… THE END")
        else:
            print("")
            print("You hadn't even decided what to do and a zombie dog ate you... THE END")
            print("Try again using the correct options marked in capital letters (EXAMPLE).")
    elif desciption_1_2 == "CALMING DOWN" or desciption_1_2 == "CALM":
        print("")
        print("You kept walking and saw a path to the side that was a bit more discreet. You followed it and reached the end of the path where you found a girl named Darling who helped you and took you to a group of survivors… THE END")
        print("")
        print("Well done, you survived!!!")
    else:
            print("")
            print("You hadn't even decided what to do and a zombie dog ate you... THE END")
            print("Try again using the correct options marked in capital letters (EXAMPLE).")
else:
     print("")
     print("You hadn't even decided what to do and a zombie dog ate you... THE END")
     print("Try again using the correct options marked in capital letters (EXAMPLE).")

print("")
print("I hope you has enjoy it, please try againg and see all the scenaris to see if you could stay human. :)")


    
    
# This is how I wrote the story before I coded it.

""""

Zombie story.
Try to survive. The options will appear in capital letters as "EXAMPLE" or as options "1 or 2".

Start…

You wake up alone in a forest in the early morning. Not far away, you see a cabin to the south, and to the north, a road leading to a bridge that takes you to a nearby city… You get up and must decide whether to go to the CABIN or the CITY.

#Scenario 1
“CABIN”
Once you're standing, you approach the cabin…
At the entrance, you see a bag next to the door… Do you want to check the bag?... YES or NO

*If (yes) scenario*
Great, you got a rusty weapon... You're standing in front of the cabin door and you hear a strange noise not far away...
You have two options:

1: GO INSIDE THE CABIN

2: GO INVESTIGATE THE NOISE

*Option 1*
You rush into the cabin and as you close the door, you are struck by something unknown and devoured by zombies…. THE END

*Option 2*
As you approach stealthily through the trees, you encounter some zombies… when you turn around, you see that you are surrounded… you draw your weapon, but it jams when you try to fire, and you are tragically bitten and turned into a zombie.

#Scenario 2
“CITY”
You walk calmly in that direction, and the path seems deserted…
… When you're near the bridge, you notice zombies nearby who haven't noticed you yet. You panic and must quickly choose between RUNNING or CALMING DOWN and continuing to walk.

*RUN Option*
You start running and the zombies around you notice, they chase you, and halfway across the bridge you trip and a zombie quickly bites you. You manage to escape and at the end of the bridge, not far away, you see a person who doesn't appear to be a zombie.
Option 1: Talk to the person.
Option 2: Turn around and continue on your way through the city.
	
*Option 1*
You approach and, upon speaking with the person, she tells you her name is Darling and that she's a survivor, that there are more like her. But she notices you've been bitten, quickly pulls out her weapon, and shoots you. You die staring at the morning sky… THE END
*Option 2*
You wandered around all day feeling the pain of the bite, and by the end of the afternoon, you were just another zombie… THE END

*Option to CALM DOWN*
You kept walking and saw a path to the side that was a bit more discreet. You followed it and reached the end of the path where you found a girl named Darling who helped you and took you to a group of survivors… THE END
Well done, you survived!!!

"""""


# I hope you enjoy it. :)
