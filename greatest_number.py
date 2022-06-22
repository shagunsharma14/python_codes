def greatest(n,m):
    return n if n>m else m
def main():
    n,m = map(int,input("Enter n and m: ").split())
    print(greatest(n,m))
main()