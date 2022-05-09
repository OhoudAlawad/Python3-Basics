# Project 6

# Game : OOP

class Game:

    def __init__(self):
        while True:
        

            print('''

                Welcome in Our Game

                Choose one of our games

                  1: Print Odd and Even number from your List
                  2: Count Words from sentence
                  3: Print numbers from 0 to user number was input
                  4: Print Numbers that are divisible by the second number from zero to the first number 
                  5: Takes two numbers from the user and prints all numbers that are divisible to that two numbers from 0 to 100
                  Press X to Exit


            ''')
            user_choice = input('Enter Game Number: ')
            if user_choice == 'X':
                print('Good Bye o_o')
                break
            else:
                
                if int(user_choice) == 1:
                    self.OddAndEven()


                elif int(user_choice) == 2:
                    self.CountWords()



                elif int(user_choice) == 3:
                    self.PrintNumbers()


                elif int(user_choice) == 4:
                    self.Divisible()


                elif int(user_choice) == 5:
                    self.Divisible2()


    def OddAndEven(self):
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

    def CountWords(self):
        sent = input ("\nEnter your sentence")
  
        # using split() 
        # to extract words from string 

        num = sent.split()
        c = []
        for i in num:
            if (sent.count(i)>=1 and (i not in c)):
                c.append(i)
        res = len(c)        
         
        print ("\nThe number of words in string is : "   + str(res))

    def PrintNumbers(self):
        n = int(input("\nEnter number to print from 0 to that number : "))

        # iterating
        for i in range(0, n+1):
            print (i)

    
    def Divisible(self):
        n1 = int(input("\nEnter first number: "))
        n2 = int(input("\nEnter second number: "))


        for i in range(0, n1+1):
            if (i % n2) == 0:
                print (i)

        
    
    def Divisible2(self):
        n1 = int(input("\nEnter first number: "))
        n2 = int(input("\nEnter second number: "))


        for i in range(0, 101):
            if (i % n1) == 0 & (i % n2) == 0:
                print (i)



    


g1 = Game()
