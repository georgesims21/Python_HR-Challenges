#------------------------------------------------------------------------------#
# You are given three integers: a, b, and m, respectively. Print two lines.
# The first line should print the result of pow(a,b). The second line should
# print the result of pow(a,b,m).
# Input Format:
#     The first line contains a, the second line contains b, and the third line
#     contains m.
# Constraints:
#     1 <= a <= 10
#     1 <= b <= 10
#     2 <= m <= 1000
#------------------------------------------------------------------------------#

a = int(input())
b = int(input())
m = int(input())

if m < 0:
    print(pow(a, b))
else:
    print(pow(a, b))
    print(pow(a, b, m))
