def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
def main():
    n = int(input("Enter the value of n: "))
    print(fact(n))
main()
