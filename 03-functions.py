# functions


'''
def mysum(x,y): # arguments  ,  parameters
    x = 3
    y = 4

    print(x+y)
mysum(3,4)

'''


#parameters

'''

    required
    keyword = positional
    default
    variable length

'''
'''
def mysum(y,x=0):
    print(x+y)

mysum(12)

'''
'''
# functions structure
def func_name(parameters):
    func_body : logic
    return target

def mysum(x,y):
    result = x+y
    #print(result)
    return result
x = mysum(3,4)
print(f'x = {x}')

# local VS Global

f = 0
print(f)  # 0


def do():
    global f
    f = 5 #local
    print(f)  # 5 

do()
print(f)  # 0

'''
'''

# anonymous function

# mysum = lambda parameters : logic
mysum = lambda x,y : x+y

x = mysum(3,4)
print(x)
'''

# function examples :
'''

    print()
    type()
    range()
    enumerate()

'''

for index , x in enumerate( range(10,20,3),1):
    print(index,x)

    
