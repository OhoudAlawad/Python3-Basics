#Encapsulation: self
## Inheritance
class Calc:
    def __init__(self,name):
        print(f'Welcome {name}')
        
    def sum(self,x,y):
        return x+y

    def mul(self,x,y):
       return x*y
'''
c1 = Calc()
print(c1.sum(2,3))
print(c1.mul(2,3))
'''

class SciCalc(Calc):

    def power(self,x,y):
        return x**y

v1 = SciCalc('Ahmed')

print(v1.sum(2,3))
print(v1.mul(3,4))
print(v1.power(2,3))



    
class A:
    def do(self):
        print('in A')

class B(A):
    pass

class C:
    def do(self):
        print('in C')

class D(B,C):
    pass

dv = D()
dv.do()

print(D.mro())
    
