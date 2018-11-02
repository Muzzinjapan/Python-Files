import random

#### PART 1 ####
## FUNCTION TO FIND THE SMALLEST OF 3 VALUES ##

def min3(x,y,z):
    if x > y:
        if y > z:
            smallest = z
        else:
            smallest = y
    else:
        if x > z:
            smallest = z
        else:
            smallest = x
    return smallest


#### PART 2 ####
## FUNCTION TO DRAW BOXES OF A SPECIFIED SIZE ##

def box(x,y):
    for height in range(x):
        for width in range(y):
            print("*", end="")
        print()


#### PART 3 ####
## FUNCTION TO FIND RETURN THE POSITION OF A VALUE IN A LIST ##

my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

def find(x,y):
    for item in range(len(x)):
        if x[item] == y:
            matched = item
            print("Found " + str(y) + " at position " + str(matched))

#### PART 4 ####
##

def create_list(number):
    my_list=[]
    for item in range(number):
        my_list.append(random.randrange(1,7))
    return my_list

def count_list(my_list,key):
    count = 0
    for item in range(len(my_list)):
        if my_list[item] == key:
            count = count + 1
    return count

def average_list(my_list):
    total_sum = 0
    for item in range(len(my_list)):
        total_sum = total_sum + my_list[item]
    average = total_sum / len(my_list)
    return(average)

main_list = create_list(10000)
for i in range(1,7):
    print("The number " + str(i) + " appears " + str(count_list(main_list,i)) + " times.")
print()
print("The average of all the values is " + str(average_list(main_list)))
