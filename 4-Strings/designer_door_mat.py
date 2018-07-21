#------------------------------------------------------------------------------#
# Mr. Vincent works in a door mat manufacturing company. One day, he designed
# a new door mat with the following specifications:
#     * Mat size must be N x M. (N is an odd natural number, and M is 3 times N)
#     * The design should have 'WELCOME' written in the center.
#     * The design pattern should only use |, . and - characters.
# Input Format:
#     A single line containing the space separated values of N and M.
# Constraints:
#     5 < N < 101
#     15 < M < 303
# Output Format:
#     Output the design pattern.
#------------------------------------------------------------------------------#

def welcomeFunc(w, l, dash, wArray):
    tempW = w - 7 # WELCOME == 7 chars
    tempW = tempW / 2 # For one side
    for i in range(int(tempW)):
        wArray.insert(0, dash)
        wArray.append(dash)
    for ii in range(len(wArray)):
        print(wArray[ii], end=""),

def upAndDown(w, l, dividor, dash):
    tempL = l - 1 # Welcome line == 1 line
    tempL = tempL / 2
    for i in range(tempL):
        

wArray = ["WELCOME"]
dividor = [".|."]
dash = "-"

length = int(input())
width = int(input())

welcomeFunc(width, length, dash, wArray)
