def greates(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
def main():
    a,b,c = map(int,input("Enter a, b, c: ").split())
    print(greates(a,b,c))
main()
