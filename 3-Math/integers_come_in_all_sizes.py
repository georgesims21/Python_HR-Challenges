#------------------------------------------------------------------------------#
# Integers in Python can be as big as the bytes in your machine's memory. There
# is no limit in size as there is: pow(2, 31) - 1(c++ int) or pow(2, 63) - 1
# (C++ long long int).
# As we know, the result of pow(a, b) grows really fast with increasing b.
# Let's do some calculations on very large integers.
# Task:
#   Read four numbers, a, b, c, d, and print the result of pow(a, b) +
#   pow(c, d).
# Input Format:
#   Integers a, b, c, and d are given on four separate lines, respectively.
# Constraints:
#   1 <= a, b, c, d <= 1000
# Output Format:
#   Print the result of on one line.
#------------------------------------------------------------------------------#

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(pow(a, b) + pow(c, d))