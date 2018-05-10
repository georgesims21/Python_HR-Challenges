#------------------------------------------------------------------------------#
# Given an integer, n, perform the following conditional actions:
#
#    If n is odd, print Weird
#    If n is even and in the inclusive range of 2 to 5, print Not Weird
#    If n is even and in the inclusive range of 6 to 20, print Weird
#    If n is even and greater than 20, print Not Weird
#------------------------------------------------------------------------------#

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
