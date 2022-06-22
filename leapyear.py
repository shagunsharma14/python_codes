def year(n):
    if n%400==0 or (n%100!=0 and n%4==0):
        print("It's a leap year")
    else:
        print("Not a leap year")

def main():
    n=int(input("Enter the year: "))
    year(n)
main()