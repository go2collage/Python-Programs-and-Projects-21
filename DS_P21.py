# Python Program / Project

def FibSearch(dict1, key, n):
    b = 0
    a = 1
    f = b + a
    while(f < n):
        b = a
        a = f
        f = b + a
        offset = -1
    while(f>1):
        i = min(offset+b, n-1)
        if(dict1[i]<key):
            f = a
            a = b
            b = f - a
            offset = i
        elif (dict1[i]>key):
            f = b
            a = a - b
            b = f - a

        else:
            return i
    if( a and dict1[offset+1] == key):
        return offset + 1
    return -1    

# Driver code

dict1 = {}
while (True):
    print("********** Menu **********")
    print("1. Fibonacci Search.")
    print("2. Exit.")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        num = int(input("Enter How many students: "))
        for i in range(num):
            data = input("Enter student name: ")
            num = int(input("Enter student phone no: "))
            dict1[num] = data
        print("Student phone number and name: ")
        print(dict1)
        list1 = dict1.keys()
        list1 = list(list1)
        list1.sort()
        print("Sorted List is: ",list1)

        key = int(input("Enter phone number to search: "))
        index = FibSearch(list1, key, num)
        if index<0:
            print("{} was not found.".format(key))
        else:
            print("{} was found at index {}.".format(key,index))
            print("Details of numbers found: ", dict1[key])
        

    elif ch == 2:
        print("You have Exit.")
        exit()

    else:
        print("Invalid choice.")

#Rahul       Modi        Mamta       Abdul
#986,        125,        209,        937