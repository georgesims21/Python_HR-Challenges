#------------------------------------------------------------------------------#
# Consider a list (list = []). You can perform the following commands:
#     insert i e: Insert integer e at position i.
#     print: Print the list.
#     remove e: Delete the first occurrence of integer e.
#     append e: Insert integer e at the end of the list.
#     sort: Sort the list.
#     pop: Pop the last element from the list.
#     reverse: Reverse the list.
# Initialize your list and read in the value of followed by lines of commands
# where each command will be of the 7 types listed above. Iterate through each
# command in order and perform the corresponding operation on your list.
# Input Format:
#     The first line contains an integer, , denoting the number of commands.
#     Each line of the subsequent lines contains one of the commands described above.
# Constraints:
#     The elements added to the list must be integers.
# Output Format:
#     For each command of type print, print the list on a new line.
#------------------------------------------------------------------------------#

theList = []

for i in range(int(input())):
    userChoice = input().split() #Splits input into seperate variables
    for iiii in range(1,len(userChoice)):
        userChoice[iiii] = int(userChoice[iiii]) #Converts str into ints
    if(userChoice[0] == "insert"):
        theList.insert(userChoice[1], userChoice[2])
    elif(userChoice[0] == "print"):
        print(theList)
    elif(userChoice[0] == "remove"):
        theList.remove(userChoice[1])
    elif(userChoice[0] == "append"):
        theList.append(userChoice[1])
    elif(userChoice[0] == "sort"):
        theList.sort()
    elif(userChoice[0] == "pop"):
        theList.pop()
    elif(userChoice[0] == "reverse"):
        theList.reverse()
