def sum(n,m):
    sum = 0
    for i in range(n,m+1):
        sum+=i
    return sum

def main():
    n,m = map(int,input("Etner n and m: ").split())
    print(sum(n,m))
main()