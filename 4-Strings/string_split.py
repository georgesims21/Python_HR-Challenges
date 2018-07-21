#------------------------------------------------------------------------------#
# Task:
# You are given a string. Split the string on a " " (space) delimiter and join
# using a - hyphen.
# Input Format:
#   The first line contains a string consisting of space separated words.
# Output Format:
#   Print the formatted string as explained above.
#------------------------------------------------------------------------------#

a = input()
a = a.split(" ")
a = "-".join(a)

print(a)
