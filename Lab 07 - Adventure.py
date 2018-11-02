## LAB 7 - ADVENTURE
## Mr Herbert
## 2018-09-12

import pygame

room_list = []

room = ("You are in a room. There is a door to the East",None,1,None,None)
room_list.append(room)

room = ("You are in a long hallway. The hallway extends North. There are doors to the East and West.",4,2,None,0)
room_list.append(room)

room = ("You are in a Dining room",5,None,None,1)
room_list.append(room)

room = ("You are in a bedroom.",None,4,0,None)
room_list.append(room)

room = ("You are in a long hallway. The hallway extends South. There are doors to the North, East and West.",6,5,1,3)
room_list.append(room)

room = ("You are in a Kitchen.",None,None,2,4)
room_list.append(room)

room = ("You are outside on a balcony.",None,None,4,None)
room_list.append(room)

current_room = 0

done = False

while done == False:
    print()
    print(room_list[current_room][0])

    move = input("What do you want to do?")
    move = move.upper()

    if move == "Q":
        done = True

    if move == "N":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("Sorry. You can't go that way.")
        else:
            current_room = next_room

    elif move == "E":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("Sorry. You can't go that way.")
        else:
            current_room = next_room

    elif move == "S":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("Sorry. You can't go that way.")
        else:
            current_room = next_room

    elif move == "W":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("Sorry. You can't go that way.")
        else:
            current_room = next_room
            
