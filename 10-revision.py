## 1 : multiplication table
'''
def multiplication_table(start,end,step_start , step_end):
    for mn in range(start,end+1):
        for x in range(step_start,step_end+1):
            print(f"{mn} X {x} = {mn*x}")
        print('------------------')

multiplication_table(2,8,5,10)


## remove duplicated char


word = input('Enter a Word: ')
chars = []
for ch in word:
    if ch not in chars:
        print(ch,end='')
        chars.append(ch)
'''

# Game : OOP

class Game:

    def __init__(self):
        while True:
        

            print('''

                Welcome in Our Game

                Choose one of our games

                  1: multiplication table
                  2: remove duplicate
                  Press X to Exit


            ''')
            user_choice = input('Enter Game Number: ')
            if user_choice == 'X':
                print('Good Bye o_o')
                break
            else:
                
                if int(user_choice) == 1:
                    start = int(input('Enter Start : '))
                    end = int(input('Enter End : '))
                    step_start =int(input('Enter Step Start : '))
                    step_End = int(input('Enter Step End : '))
                    self.multiplication_table(start,end,step_start,step_End)
                elif int(user_choice) == 2:
                    self.remove_duplicate()
            


    def multiplication_table(self,start,end,step_start , step_end):
        for mn in range(start,end+1):
            for x in range(step_start,step_end+1):
                print(f"{mn} X {x} = {mn*x}")
            print('------------------')         
                                
    def remove_duplicate(self):
        word = input('Enter a Word: ')
        chars = []
        for ch in word:
            if ch not in chars:
               print(ch,end='')
               chars.append(ch)         
                        
                    




g1 = Game()
