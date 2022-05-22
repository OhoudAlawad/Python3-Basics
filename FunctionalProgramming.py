# map
'''
names =['maha','Asma','Frah']
mycount =[]
for name in names:
    mycount.append(len(name))
print(mycount)
'''
'''
names =['maha','Asma','Frah']

def get_length(x):
    return len(x)
mycount = map(get_length,names)
print(list(mycount))

''' 

# filter
'''
from unittest import result


numbers =  [12,30,10,5,1000,500,80]

def myfilter(x):
    if x > 50 :
        return True
    else:
        return False

result = filter(myfilter,numbers)
print(list(result))
'''

# reduce 
'''
import functools
import numbers
def mysum(x,y):
    return x+y

numbers = [12,30,10,5,1000,500,80]

print(functools.reduce(mysum,numbers))
'''

# str join

'''
names =['maha','Asma','Frah']
name = ' '.join(names)
print(name)
'''
'''
path = "my    name       is     Ohoud"
print(path.split())
'''

path = "my  ****name *****is ***** Ohoud"
print(path.replace('*','').split())