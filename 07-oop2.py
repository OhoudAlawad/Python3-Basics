'''
    -add student : name , Welcome message
    - add mark to student
    - get avg marks
'''

class Student:
    def __init__(self, name):
        print(f'Welcome {name}')
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def get_avg(self):
        return sum(self.marks)/len(self.marks)



s1 = Student('Ahmed')

s1.add_mark(30)
s1.add_mark(90)
s1.add_mark(50)
s1.add_mark(80)
s1.add_mark(20)
s1.add_mark(40)

print(s1.marks)
print(s1.get_avg())

s2 = Student('ali')

s2.add_mark(80)
s2.add_mark(30)
s2.add_mark(60)
s2.add_mark(20)
s2.add_mark(70)

print(s2.marks)
print(s2.get_avg())

