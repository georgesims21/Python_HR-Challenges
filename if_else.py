integer = input("Enter Number: ")

if(integer % 2 != 0):
    print("Weird")
else:
    if(2 <= integer <= 5):
        print("Not Weird")
    elif(6 <= integer <= 20):
        print("Weird")
    else:
        print("Not Weird")
