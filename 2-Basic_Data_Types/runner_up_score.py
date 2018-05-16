#------------------------------------------------------------------------------#
# Given the participants' score sheet for your University Sports Day, you are
# required to find the runner-up score. You are given n scores. Store them in a
# list and find the score of the runner-up.
# Input Format:
#   The first line contains n. The second line contains an array A[] of n
#   integers each separated by a space.
# Constraints:
#   2 <= n <= 10
#   -100 <= A[i] <= 100
# Output Format:
#   Print the runner-up score.
#------------------------------------------------------------------------------#

myArray = []
howMany = int(input())
someVariable = input().split()
for i in range(0, len(someVariable)):
    someVariable[i] = int(someVariable[i])  # Convert str to int

someVariable.sort()  # Sort numerically
someVariable.reverse()

highest = someVariable[0]

for ii in range(0, len(someVariable)):
    if(someVariable[ii] < highest):
         print(someVariable[ii])  # Print the second largest int
         break
