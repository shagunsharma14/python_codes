def lsearch(arr,item):
    for i in range(len(arr)):
        if arr[i]==item:
            return i
    return -1
def main():
    n = int(input("Enter the value: "))
    arr = [34,65,98,234,23,12,97]
    length = len(arr)
    s = lsearch(arr,n)
    if s==-1:
        print("not found")
    else:
        print("val {} found at index {}".format(n,s))

main()