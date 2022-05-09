# Project 4
# Print Numbers that are divisible by the second number from zero to the first number 

n1 = int(input("\nEnter first number: "))
n2 = int(input("\nEnter second number: "))


for i in range(0, n1+1):
    if (i % n2) == 0:
        print (i)
