'''
avl = 10
i=1
x = int(input("Enter number of candies you want"))
while i<=x:
    if i> avl:
        print('Out of Stock')
        break
    print('candies')
    i+=1

print('See you later')
'''
'''
count=0
for i in range(1,100):
    if i%3==0:
        continue

    print(i)
    count+=1
    i+=1
print(count)
'''
'''
for i in range(1,100):
    if(i%2!=0):
        pass
    else:
        print(i)

print('bye')
'''
'''
count=0
n1 =0
n2 = 1
print(n1)
print(n2)
for i in range(2,100):
    if count == 50:
        break
    nth = n1+n2
    print(nth)
    count+=1
    i+=1
    n1 = n2
    n2 = nth
print(count)
'''
#to check weatehr prime number or not

x = int(input('Enter Number'))

if x>1:
    for i in range(2, x):

        if x%i==0:
            print('not a primenumber')
            break
        else:
            print('primenumber')
