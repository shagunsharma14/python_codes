"""
color = ['red','yellow','green']
fruit = ['Apple','Mango','Banana']

for x in color:
    for y in fruit:
        print(x,y)
"""
"""
for x in range(99,9,-9):
    print(x)

"""
#All perfect squaers from 1 to 500
count=0
for i in range(1,500):
    if i*i<=500:
        print(i*i)
        count+=1
        i+=1
print()
print(count)
