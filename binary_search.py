def binary_search(arr, n, key):
    l=1
    h = n
    while (l <= h):
        mid = int((l + h) / 2)
        if key == arr[mid]:
            return mid
        if key < arr[mid]:
            h = mid - 1
        else:
            l = mid + 1
    return -1


def main():
    ls = [1, 3, 9, 11, 15, 19, 29]
    key1 = 25
    key2 = 15
    print (binary_search(ls,len(ls),key1))
    print(binary_search(ls,len(ls),key2))


main()