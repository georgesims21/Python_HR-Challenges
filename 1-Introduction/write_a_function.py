#------------------------------------------------------------------------------#
# You are given the year, and you have to write a function to check if the year
# is leap or not.
# Input Format:
#   Read y, the year that needs to be checked.
# Constraints:
#   1900 <= y <= 10^5
# Output Format
#   Your function must return a boolean value (True/False)
#------------------------------------------------------------------------------#

def leapYear(input):
    if(input % 4 == 0):
        if(input % 100 == 0):
            if (input % 400 == 0):
                return True
            return False
        return True
    else:
        return False

theYear = int(input())
print(leapYear(theYear))
