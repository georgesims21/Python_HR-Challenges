#------------------------------------------------------------------------------#
# You have a record of N students. Each record contains the student's name, and
# their percent marks in Maths, Physics and Chemistry. The marks can be floating
# values. The user enters some integer N followed by the names and marks for N
# students. You are required to save the record in a dictionary data type. The
# user then enters a student's name. Output the average percentage marks obtained
# by that student, correct to two decimal places.
# Input Format:
#   The first line contains the integer N, the number of students. The next N lines
#   contains the name and marks obtained by that student separated by a space.
#   The final line contains the name of a particular student previously listed.
# Constraints:
#   2 <= N <= 10
#   0 <= Marks <= 100
# Output Format:
#   Print one line: The average of the marks obtained by the particular student
#   correct to 2 decimal places.
#------------------------------------------------------------------------------#

studentFinalResults = {}
for i in range(int(input())):
    student = input().split()
    #  Arrange input into 1 dict key and the scores into a separate list as value
    studentFinalResults.setdefault(student[0], []).append([float(student[1]), +
    float(student[2]), float(student[3])])
searchFor = input()
#  Create average percentage score of the 3 grades
testing = float((studentFinalResults[searchFor][0][0] +
                 studentFinalResults[searchFor][0][1] +
                 studentFinalResults[searchFor][0][2]) / 3)
#  Print to 2 decimal places
print("%.2f" % testing)
