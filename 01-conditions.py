# simple condition

x = 5

if x == 3 :
    print('X = 3')

else:
    print(x)




# if elif else

x = 10

if x == 3 :
    print('X = 3')

elif x < 2 :
    print('x > 2')

elif x < 6 :
    print('x < 6')

else:
    print(x)
    


#Nested If

x = 11

if x < 10 :
    print('x < 10')

    if x < 5 :
        print('x < 5')
    else:
        print('x > 5')

else:
    print('x > 10')

    

# if with boolean operators

username = 'Ohoud'
password = 12345

if username == 'Ohoud' and password == 12345:
    print('Welcome and')

if username == 'Ohoud2' or password == 12345678:
    print('Welcome')
