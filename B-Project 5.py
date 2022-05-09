# Project 5
# A program that takes two numbers from the user and prints all numbers that are divisible to that two numbers from 0 to 100

n1 = int(input("\nEnter first number: "))
n2 = int(input("\nEnter second number: "))


for i in range(0, 100):
    if (i % n1) == 0 & (i % n2) == 0:
        print (i)
