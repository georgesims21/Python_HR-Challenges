#------------------------------------------------------------------------------#
# Task:
#    You are given a string S.
#    Your task is to find out if the string contains: alphanumeric characters,
#    alphabetical characters, digits, lowercase and uppercase characters.
# Input Format:
#    A single line containing a string S.
# Constraints:
#   0 < len(S) < 1000
# Output Format:
#   In the first line, print True if has any alphanumeric characters. Otherwise,
#   print False.
#   In the second line, print True if has any alphabetical characters. Otherwise,
#   print False.
#   In the third line, print True if has any digits. Otherwise, print False.
#   In the fourth line, print True if has any lowercase characters. Otherwise,
#   print False.
#   In the fifth line, print True if has any uppercase characters. Otherwise,
#   print False.
#------------------------------------------------------------------------------#

boolArray = [False, False, False, False, False]

string = input()

for char in string:
    if(char.isalnum()):
        boolArray[0] = True # isNumeric
    if(char.isalpha()):
        boolArray[1] = True # isAlphabet
    if(char.isdigit()):
        boolArray[2] = True # isDigit
    if(char.islower()):
        boolArray[3] = True # isLower
    if(char.isupper()):
        boolArray[4] = True # isUpper

for i in range(5):
    print(boolArray[i])
