==''
newArr = array(vals.typecode,(a for a in vals))
for x in newArr:
    print(x,end="\t")
print('\n')
newArr1 = array(newArr.typecode,(b*b-b for b in newArr))
for x in newArr1:
    print(x,end="\t")
'''
#Sorting elements of a given array
'''
from array import *
vals = array('i',[1011,121,397,439,1335])
a =0

for i in range(len(vals)):
    print(vals[i])
    for j in range(i+1,len(vals)):
        print(vals[j])
        if(vals[i]>vals[j]):
            (vals[i],vals[j]) = (vals[j],vals[i])
            print("i is:",vals[i])
            print("j is:",vals[j])
            print()
for i in range (len(vals)):
    print(vals[i])

'''
'''
#Taking Input from the user
from array import *
arr = array('i',[])
n = int(input("Enter the size of an array"))
for i in range(n):
    x = int(input("Enter the element"))
    arr.append(x)

print(arr)

key = int(input("Enther the key"))
k=0
for e in arr:
    if e==key:
        print(k)
        break
    k+=1

print(arr.index(key))
'''
'''
from numpy import *

arr = array([1,2,3],[4,5,6])
print(arr)
'''
'''
#Different ways to create an array
from numpy import *
#arr = array([1,2,3,4.0])
#arr = linspace(0,15,100)
#arr = logspace(0,15)
#arr = arange(0,15,2)
#arr = zeros(400)
arr = ones(400)
print(arr)
'''
'''
from numpy import *
from array import *
arr1 = array('i',[1,2,3,4,5])
arr2 = array('i',[6,7,8,9,10])
print(concatenate([arr1,arr2]))
arr3 = array(arr2.typecode,(a*a for a in arr1))

print(arr3)
'''
'''
from numpy import *
arr1 = arange(1,15,1)

#arr2 = arr1.view()#Shallow Copying
arr2 = arr1.copy()#Deep Copying
arr2[9] = 99
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
'''
'''
from numpy import *
arr1 = array([1,2,3,4,5],int)
arr2 = array([6,7,8,9,0],int)
arr3=0
for i in len(arr1):
    for j in len((arr2)):
        arr3 = arr1[i] +arr2[j]
        i+=1
        j+=1
print(arr3)
'''
#multidimensional array
from numpy import *
arr1 = array([[1,2,3,4],[5,6,7,8]])
print(matrix(arr1))
m1 = matrix('1,2,3;4,5,6;7,8,9')
m2 = matrix('9,8,7;6,5,4;3,2,1')
m3 = m1*m2
print(m3)





















