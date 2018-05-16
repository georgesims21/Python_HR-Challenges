#------------------------------------------------------------------------------#
# Given an integer, n, and space-separated integers as input, create a tuple, t,
# of those integers. Then compute and print the result of hash(t).
# Note: hash() is one of the functions in the __builtins__ module, so it need
# not be imported.
# Input Format:
#   The first line contains an integer, n, denoting the number of elements in
#   the tuple.
#   The second line contains n space-separated integers describing the elements
#   in tuple .
# Output Format:
#   Print the result of hash(t).
#------------------------------------------------------------------------------#

theTuple = ()
amountOfInts = input()
userChoice = input().split() #Splits input into seperate variables
for ii in range (0, len(userChoice)):
    userChoice[ii] = int(userChoice[ii]) #Converts each str to int
theTuple = tuple(userChoice) #Create tuple from list
print(hash(theTuple))
