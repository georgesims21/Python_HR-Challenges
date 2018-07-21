#------------------------------------------------------------------------------#
# In this challenge, the user enters a string and a substring. You have to print
# the number of times that the substring occurs in the given string. String
# traversal will take place from left to right, not from right to left.
# NOTE: String letters are case-sensitive.
#
# Input Format:
#     The first line of input contains the original string. The next line contains
#     the substring.
#
# Constraints:
#     1 <= length(string) <= 200
#     Each character in the string is an ascii character.
#
# Output Format
#     Output the integer number indicating the total number of occurrences of the
#     substring in the original string.
#------------------------------------------------------------------------------#

actualString = input()
subString = input()

index = 0
counter = 0

while index < len(actualString):
    # Returns index if subString is found
    index = actualString.find(subString, index)
    # Avoids infinite loop 
    if(index == -1):
        break
    index += 1
    counter += 1
print(int(counter))
