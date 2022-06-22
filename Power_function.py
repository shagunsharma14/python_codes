def pow(x,n):
    if n==0:
        return 1
    else:
        return x*pow(x,n-1)

def main():
    x,n = map(int,input("Enter x and y: ").split())
    if n<0:
        print("Enter the valid input")
    else:
        print(pow(x,n))

main()