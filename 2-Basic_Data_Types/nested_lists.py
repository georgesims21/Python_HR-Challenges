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

gradesList = []

for i in range(int(input())):
    name = input()
    grade = float(input())
    gradesList.append([grade, name])  # Create nested list for each student

gradesList.sort()  # Sort numerically ascending
lowest = gradesList[0][0]
newList = []

for ii in range(len(gradesList)):
    if gradesList[ii][0] > lowest:
        newVariable = gradesList[ii][0]  # Assign second lowest value to variable
        for iii in range(ii, len(gradesList)):  # Avoid checking lowest
            if gradesList[iii][0] == newVariable:
                newList.append(gradesList[iii][1])  # Append to new list all of the second lowest values
        break
newList.sort()  # Sort alphabetically
for item in newList:
    print(item)