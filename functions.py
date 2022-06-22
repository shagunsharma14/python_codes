'''
def greet():
    print("Hello")
    print("Good Morning")
#end of function


greet()
def add_sub(x,y):
    a = x+y
    s = x-y
    return a,s

result1,result2 = add_sub(4,6)

print(result1)
print(result2)
'''
#In Python there's no such thing like call by value of call by reference it totally depends on the type of variable that it is mutuable or immutable
#if intereger of string then it value won't change afeter the implemetation of the function but if the variable type if mutuable like list or array etc then the
#original value will also change
'''
#immutuable example
def update(x):
    print("add of x: ",id(x))
    x= 10
    print("x: ",x)
a= 9
print("add of a: ",id(a))

update(a)
print("a: ",a)
'''
'''
#example for mutuable data type
def update(x):
    x[1] = 99
    print("updated lis: ",lis)
lis = [1,2,3]
print("lis:",lis)
update(lis)
print(" lis: ",lis)
'''
#Type of arguments
#1.Position 2.Keyword 3.Default 4.argument_length
#By Position
'''
def add(a,b):
    c= a+b
    print(c)
    
add(4,9)
'''
#By keyword
'''
def detail(age,name):
    print(age)
    print(name)

detail(name='Shagun',age='21')
'''
#By Default
'''
def detail(name,age=18):
    print(age)
    print(name)

detail(name='Shagun')
'''
'''
#4.Argument Length
def add(*b):
    c = 0
    for e in b:
        c= c+e
    print(c)

add(4, 9,10,11,12)
'''
'''
#Keyworded Variable length argument
def person(name,**data):
    print('name ',name)
    for k,w in data.items():
        print(k,w)




person(name='Shgaun',phno=6005440532,age=21,hobbie1='Programing',hobbie2='Gym'
'''
'''
#even or odd numbers in a list
def count(lis):
    ecount=0
    ocount=0
    for e in lis:
        if e%2==0:
            ecount+=1
        else:
            ocount+=1
    return ecount,ocount
#lis = list(input('Enter the list element'))
lis = [1,2,3,4,5,6,7,8,9]
even,odd =count(lis)
print("even: {} and odd: {}".format(even,odd))
'''
#counting number of users havae name length more than 5
'''
def count(names):
    ncount=0
    for e in names:
        if len(e)+1 >5:
            ncount+=1
    return ncount
x=0
n = int(input('enter the length of list: '))
names=[]
for i in range(n):
    x = str(input('enter name'))
    names.append(x)


print("names greater than length 5: ",count(names))
'''
'''
#fib without recurssion
def fib(n):
    if n<0:
        print('invalid input')
        return
    a=0
    b=1

    if n==1:
        print(a)
    print(a)
    print(b)
    if n>2:
      for i in range(2,n):
          c = a + b
          print(c)
          a = b
          b = c

fib(10000)
'''
'''
#find the factorial of a number
def fact(x):
    f=1
    for i in range(1,x+1):
        f = f*i
    return f
res = fact(5)
print(res)

'''
'''
#recurssion in python
import sys
print(sys.setrecursionlimit(100000))
print(sys.getrecursionlimit())
i=0
def greet():
    global i
    i += 1
    print('hello: ',i)

    greet()
greet()
'''
'''
#factorial using recurssion
def fact(n):
    if n==0:
        return 1

    return n*fact(n-1)

print(fact(50))
'''
'''

#lambda function
#we use lambda function when we need to use a particular function only once and not more than that so to save number of lines in a code we use lambda function

lis = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda f: f%2==0,lis)))
'''

'''
#1.filter() to filter a value filter(function,sequence) it'll take single parameter n:n+ny
lis = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda n:n%2==0,lis)))
'''


#2.map()  to perform an operation   map(functon,sequence) it'll take single parameter n: n+n
'''
lis = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda n:n+2,lis)))
'''


#3.reduce() to reduce  it is stored in functools  reduce(fucnction,sequence) it'll take two parameters lambda a,b: a+b and return a single answer
#f = lambda a,b: a*b
#print(f(5,3))
'''
import functools
lis = [1,2,3,4,5,6,7,8,9]
print(functools.reduce(lambda a,b: a+b,lis))
'''

#Decorators /functions who take functions as an argument
def div(a,b):
    return a/b

#decorator
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
    return inner

div1=smart_div(div)
print(div1(2,4))






