#Program 2: Addition Quiz
#Create a program that automatically generate two random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct answer
#The program will ask the user 10 addition operation
#Display the result summary of the 10 operations (ex 9/10)

import random

def intro():
    print("Welcome to my Math Quiz!")
    name= input("Please enter your name: ")
    print(f"\nHi, {name}! All the best!\n")
    return name

def add():
    student_score= 0
    while True: 
        num1= random.randint (0,99)
        num2= random.randint (0,99)
        print("What is " + str(num1) + " plus " + str(num2)+ "?")
        answer = int(input("What is your answer?: "))
        if answer == (num1 + num2):
            print("Correct! You got it right! :)\n")
            student_score +=1
        else:
            print("Ooops! Incorrect. The right answer is " + str(num1+num2) + ".\n") 
            student_score -= 2
        if student_score < 0:
            student_score = 0

        print("Student has a score of " + str(student_score) + ".")

intro()
add() 