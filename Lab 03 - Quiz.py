## Assessment 03 - A Quiz
## Created by Mr Herbert
## April 2018


## Print a line welcoming the user to the quiz and
## set their score to zero.
print("Welcome to the Quiz!")
score = 0

## Ask the first question and get their answer.
print("Question 1")
answer_1 = input("What does 3 x 4 = :")

## Evaluate whether or not their answer was correct.
## If it were correct, let them know and add 1 to their score.
## If they were wrong, let them know.
if answer_1 == "12":
    print("correct!")
    score = score + 1
else:
    print("Incorrect!")

## Let them know their current score.
print("Your current score is",score,"/ 5")

## Ask the second question and get their answer.
print("Question 2")
answer_2 = input("What is the opposite of hot?")

## Evaluate whether or not their answer was correct.
## If it were correct, let them know and add 1 to their score.
## If they were wrong, let them know.
if answer_2 == "cold":
    print("correct!")
    score = score + 1
else:
    print("Incorrect!")

## Let them know their current score.
print("Your current score is",score,"/ 5")

## Ask the third question and get their answer.
print("Question 3")
print("Who was a founding memeber of Apple?")
print("  A: Bill Gates")
print("  B: Steve Jobs")
print("  C: Mark Zuckerberg")
print("  D: None of the above")
answer_3 = input("A, B, C or D:")

## Evaluate whether or not their answer was correct.
## If it were correct, let them know and add 1 to their score.
## If they were wrong, let them know.
if answer_3 == "B" or answer_3 == "b":
    print("correct!")
    score = score + 1
else:
    print("Incorrect!")

## Let them know their current score.
print("Your current score is",score,"/ 5")

## Ask the second question and get their answer.
print("Question 4")
answer_4 = input("How many degrees in a circle?")

## Evaluate whether or not their answer was correct.
## If it were correct, let them know and add 1 to their score.
## If they were wrong, let them know.
if answer_4 == "360":
    print("correct!")
    score = score + 1
else:
    print("Incorrect!")

## Let them know their current score.
print("Your current score is",score,"/ 5")

## Ask the second question and get their answer.
print("Question 5")
answer_5 = input("What do you call a baby cat?")

## Evaluate whether or not their answer was correct.
## If it were correct, let them know and add 1 to their score.
## If they were wrong, let them know.
if answer_5 == "kitten" or answer_5 == "Kitten" or answer_5 == "a kitten" or answer_5 == "a Kitten":
    print("correct!")
    score = score + 1
else:
    print("Incorrect!")

## Let them know their current score.
print("Your current score is",score,"/ 5")

## Tell them their final percentage
print()
print("Your final percentage is",score/5*100,"%")
