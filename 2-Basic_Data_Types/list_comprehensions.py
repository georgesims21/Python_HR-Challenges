#------------------------------------------------------------------------------#
# Let's learn about list comprehensions! You are given three integers x, y and z
# representing the dimensions of a cuboid along with an integer n. You have to
# print a list of all possible coordinates given by on a 3D grid where the sum
# of i + j + k is not equal to n. Here, 0 <= i <= x;0 <= j <= y;0 <= k <= z
# Input Format:
#   Four integers and each on four separate lines, respectively.
# Constraints:
#   Print the list in lexicographic increasing order.
#------------------------------------------------------------------------------#

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# #Prints 3D co-ords, skipping (i + j + k = n)
# print [ [ i, j, k]] for i in range(x + 1) for j in range(y + 1) for k in
# range(z + 1) if ((i + j + k) != n ) ]



x, y, n = int(input().split())

ar = []
p = 0
for i in range (x + 1 ):
   for j in range(y + 1):
       if i+j != n:
           ar.append([])
           ar[p] = [ i , j ]
           p+=1

print (ar)
