#------------------------------------------------------------------------------#
# Task:
#   Read a given string, change the character at a given index and then print
#   the modified string.
# Input Format:
#   The first line contains a string, S.
#   The next line contains an integer i, denoting the index location and a
#   character separated by a space.
# Output Format:
#   Print the formatted string, replace the character at index with character c.
#------------------------------------------------------------------------------#

string = input()
temp = input().split()
position = int(temp[0])
replacement = temp[1]

string = string[:position] + replacement + string[position + 1:]

print(string)
