def isprime(n):
    flag=0
    for i in range(2,n):
        if n%i==0:
            flag=1
            break
    if n<2:
        flag=1
    if flag==1:
        print("not prime number")
    else:
        print("prime number")

def main():
    n=int(input("Enter the number: "))
    isprime(n)
main()