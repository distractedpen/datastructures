#basic operations for arrays
a = [1, 3, 4, 6, 8]
n = 5 #size of the array

#Psudocode
#1. START
#2. Repeat 3 and 4 while n < array length
#3. display array[n]
#4. n <- n + 1
#5. STOP
#Traverse is O(n)
def traverse(arr):
    print("The original array elements are: ")
    for i in range(n):
        print("a[{0}] = {1}".format(i, arr[i]))


#Psudocode for insertion to front of array
#1. START
#2. IF N = MAX, return
#3. ELSE
#4.     N = N + 1
#5.     FOR ALL ELEMENTS IN A
#6.         MOVE TO NEXT ADJACENT LOCATION
#7.     A[FIRST] = NEW_ELEMENT
#8. STOP
#
#Psudocode for insertion at index
#1. START
#2. IF N = MAX, return
#3. Else
#4.     N = N + 1
#5.     SEEK Location index
#6.     FOR ALL ELEMENTS A[index] TO A[N]
#7.         MOVE TO NEXT ADJACENT LOCATION
#8.     A[index] = NEW_ELEMENT
#9. STOP
#
#Psudo code for insertion before/after is similar to previous
#change in 6. and 8.
#before: A[index] becomes A[index - 1]
#after: A[index] becomes A[index + 1]
def insert(item, index):
    global n
    global a
    print("\nThe original array elements are: ")
    for i in range(n):
        print("a[{0}] = {1}".format(i, a[i]))
    #insert at the end
    if (index == n):
        n += 1
        b = [None for i in range(n)]
        for i in range(n-1):
            b[i] = a[i]
        b[n-1] = item
        a = b
    #insert at the front or in the middle
    elif 0 <= index < n:
        n += 1
        b = [None for i in range(n)]
        for i in range(0, index):
            b[i] = a[i]
        b[index] = item
        for i in range(index, n-1):
            b[i+1] = a[i]
        a = b

    print("\nThe new array elements are: ")
    for i in range(n):
        print("a[{0}] = {1}".format(i, a[i]))

def main():
    traverse(a)
    insert(0, 5) #insert at the end
    insert(5, 2) #insert in the middle
    insert(9, 0) #insert at the beginning

if __name__ == "__main__":
    main()
