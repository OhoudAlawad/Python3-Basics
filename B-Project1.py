## Project 1 ##

# creating an empty lists
odd = []
even = []

# number of elements as input
n = int(input("\nEnter number of elements : "))

# iterating
for i in range(0, n):
        num = int(input("\nEnter the number : "))
        if (num % 2) == 0:
                even.append(num)
        else:
            odd.append(num)
        

print("\nThe list of even numbers is: " , even)

print("\nThe list of odd numbers is: ", odd)
