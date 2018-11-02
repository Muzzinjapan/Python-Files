## The Camel Game
## By Mr Herbert
## April 2018


## This imports the "random" library so we can generate random numbers.
import random


## This explains the game to the user.
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and out run the natives.")


## The variable done is set to "False" as long as the game runs. If the user dies, the
## camel dies, the natives catch us or we cross the desert then it is set to "True" and
## the game ends.
done = False


## This section sets all our variables for the game.
kilometres_travelled = 0
thirst = 0
camel_tiredness = 0
native_distance = -20
canteen_drinks = 5


## This loop will continue until done is set to "True".
## At the start of each loop the options are presented and the user can select one option.
while not done:
    print()
    print("  A. Drink from your canteen.")
    print("  B. Ahead moderate speed.")
    print("  C. Ahead full speed")
    print("  D. Stop for the night")
    print("  E. Status check")
    print("  Q. Quit")
    print()

    response = input("What would you like to do? ")


## If the user selects Q then the game quits.
    if response.upper() == "Q":
        done = True


## If the user selects E then we display the current status of some key variables.
    elif response.upper() == "E":
        print()
        print("Kilometres travelled:",kilometres_travelled)
        print("Drinks in canteen:",canteen_drinks)
        print("The natives are",kilometres_travelled - native_distance,"kilometres behind you")


## If the user selects D then we reset the camel tiredness and increase the native's distance.
    elif response.upper() == "D":
        camel_tiredness = 0
        print()
        print("The camel is happy!")
        native_distance += random.randrange(7,14)


## If the user selects C then we increase the amount travelled by both the user and the natives.
## We also make the camel more tired, ourselves more thirsty and have a chance to hit an oasis.
    elif response.upper() == "C":
        travel_burst = random.randrange(10,20)
        kilometres_travelled += travel_burst
        thirst += 1
        camel_tiredness += random.randrange(1,3)
        native_distance += random.randrange(7,14)
        print()
        print("You have travelled",travel_burst,"kilometres")
        oasis = random.randrange(1,20)
        if not done and oasis == 1:
            print()
            print("You found an oasis!")
            canteen_drinks = 5
            thirst = 0
            camel_tiredness = 0


## If the user selects B then we increase the amount travelled by both the user and the natives.
## We also make the camel more tired, ourselves more thirsty and have a chance to hit an oasis.
    elif response.upper() == "B":
        travel_burst = random.randrange(5,12)
        kilometres_travelled += travel_burst
        thirst += 1
        camel_tiredness += 1
        native_distance += random.randrange(7,14)
        print()
        print("You have travelled",travel_burst,"kilometres")
        oasis = random.randrange(1,20)
        if not done and oasis == 1:
            print()
            print("You found an oasis!")
            canteen_drinks = 5
            thirst = 0
            camel_tiredness = 0


## If the user selects A then we reset thirst and remove one drink from the canteen.
    elif response.upper() == "A":
        if canteen_drinks > 0:
            canteen_drinks -= 1
            thirst = 0
        else:
            print()
            print("Your canteen is empty!")


## If thirst ever exceeds 6 then the user dies. If it exceeds 4 we let them know they're thirsty.
    if thirst > 6:
        print()
        print("You died of thirst!")
        done = True
    elif thirst > 4:
        print()
        print("You are thirsty")


## If the camel tiredness ever exceeds 8, the camel dies. If it exceeds 5 we let them know.
    if not done and camel_tiredness > 8:
        print()
        print("Your camel is dead!")
        done = True
    elif not done and camel_tiredness > 5:
        print()
        print("Your camel is getting tired")


## If the native distance ever catches or exceeds ours then we end the game. If they come within
## 15 kilometers we let the user know.
    if not done and native_distance >= kilometres_travelled:
        print()
        print("The natives caught you!")
        done = True
    elif not done and native_distance + 15 >= kilometres_travelled:
        print()
        print("The natives are getting close!")


## If the user hits or exceeds 200km they win!
    if not done and kilometres_travelled >= 200:
        print()
        print("You made it across the desert and escaped! You Win!")
        print("The natives were",kilometres_travelled - native_distance,"kilometres behind you.")
        done = True

    
        

    
            
        
        
        
    
