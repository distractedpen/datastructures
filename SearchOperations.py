def linearSearch(array, value):
    i = 0
    for i in range(len(array)):
        if array[i] == value:
            return "Found {0} at index {1}.".format(value, i)
        i += 1
    return "{0} not found.".format(value)

def binarySearch(array, value):
    low = 0
    mid = len(array) // 2
    high = len(array) - 1
    while(low <= high):
        if array[mid] < value:
            low = mid + 1
            mid = low + (high - low) // 2
        elif array[mid] > value:
            high = mid - 1 
            mid = low + (high - low) // 2
        else:
            return "Found {0} at index {1}.".format(value, mid)
    return "{0} not found.".format(value)


def main():
    a = [0, 1, 3, 5, 6, 8]
    print(linearSearch(a, 3))
    print(linearSearch(a, 4))
    print(binarySearch(a, 1))
    print(binarySearch(a, 2))
    

if __name__ == "__main__":
    main()
