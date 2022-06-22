#Class is like a blueprint
'''if phone is a object then design of a phone is a class and phones are instances of that class'''
'''
class computer:

    def __init__(self):
        self.name = 'Naveen'
        self.age = 28

    def update(self):
        self.age =18



    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


c1=computer()
c2=computer()

c1.age = 15
c2.update()

if c1.compare(c2)==True:
    print('They are smae')
else:
    print('They are different')
    
'''
'''
#we have two types of variables in py 1.Class Variable 2.instance\object variabl
class student:
    school = 'Teachers'#class variable
    def __init__(self,m1,m2,m3):#instance varialbe
        self.m1 =m1
        self.m2 =m2
        self.m3 =m3
    def avg(self):#for instance variable use self
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):#getter
        return self.m1
    def set_m1(self,new_m1):#setter
        self.m1 = new_m1
        #use Decorators to define class variable
    @classmethod
    def info(cls):  #for class variable use cls
        return cls.school
    #if a method don't have 'cls' or 'self' as an argument then that method is known as static method
    @staticmethod
    def sc():
        print('hye! I am a Static method')

s1 =student(13,15,16)
s2 =student(98,143,123)
print(s1.avg())
print(s2.avg())
s1.get_m1()
s1.set_m1(99)
print('new_avg: ',s1.avg())
print(student.info())
print(student.sc())
#                       .......9667987711
'''
#Inheritance
class A:
    def __init__(self):
        print('init of A')
    def feature1(self):
        print('feature_1')
    def feature2(self):
        print('feature_2')
class B:

    def __init__(self):

        print('init of B')
    def feature3(self):
        print('feature_3')
    def feature4(self):
        print('feature_4')
class C(A,B):
    def __init__(self):
        super().__init__()
        print('init of C')
b = C()

#MRO it is always from left to right
