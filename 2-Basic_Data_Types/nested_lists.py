#------------------------------------------------------------------------------#
# Given the names and grades for each student in a Physics class of n students,
# store them in a nested list and print the name(s) of any student(s) having the
# second lowest grade.
# Note: If there are multiple students with the same grade, order their names
# alphabetically and print each name on a new line.
# Input Format
#   The first line contains an integer, n, the number of students.
#   The 2n subsequent lines describe each student over 2 lines; the first line
#   contains a student's name, and the second line contains their grade.
# Constraints:
#   2 <= n <= 5
#   There will always be one or more students having the second lowest grade.
# Output Format:
#   Print the name(s) of any student(s) having the second lowest grade in
#   Physics; if there are multiple students, order their names alphabetically
#   and print each one on a new line.
#------------------------------------------------------------------------------#
def testing(theList, value, index):
    newList = []
    for i in range(len(theList)):
        if(theList[i][0] == value):
            newList.append(theList[i][1])
    newList.sort()
    print(newList)
gradesList = []

for i in range(int(input())):
    name = input()
    grade = float(input())
    gradesList.append([grade, name])  # Create nested list for each student

gradesList.sort()
lowest = gradesList[0]
print(gradesList)

for ii in range(len(gradesList)):
    if(gradesList[ii] > lowest):
        testing(gradesList, gradesList[ii], ii)
        break
