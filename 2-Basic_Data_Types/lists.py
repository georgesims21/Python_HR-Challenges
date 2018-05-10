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

noLines = int(input())
theList = []

for ii in range(noLines):
    action = input()
    if(action == "insert"):
        i = int(input())
        e = int(input())
        theList[i] = e
    elif(action == "print"):
        print(theList)
    elif(action == "remove"):
        e = int(input())
        for item in items:
            if item.startswith(e):
                items.remove(item)
                break
    elif(action == "append"):
        e = int(input())
        theList.append(e)
    elif(action == "sort"):
        theList.sort()
    elif(action == "pop"):
        theList.pop()
    elif(action == "reverse"):
        theList[::-1]
