#------------------------------------------------------------------------------#
# Mr. Vincent works in a door mat manufacturing company. One day, he designed
# a new door mat with the following specifications:
#     * Mat size must be N x M. (N is an odd natural number, and M is 3 times N)
#     * The design should have 'WELCOME' written in the center.
#     * The design pattern should only use |, . and - characters.
# Input Format:
#     A single line containing the space separated values of N and M.
# Constraints:
#     5 < N < 101
#     15 < M < 303
# Output Format:
#     Output the design pattern.
#------------------------------------------------------------------------------#

def welcome_line(width):
    welcome = "WELCOME"
    temp = int((width - 7) / 2)  # WELCOME = 7 chars, / 2 for each side
    welcome = ("-" * temp) + welcome + ("-" * temp)  # Adds calculated amount of "-"'s to each side of WELCOME
    return welcome

def pattern_line(width, counter):
    pattern = ".|."
    new_pattern = (".|." * counter) + pattern + (".|." * counter)  # Evenly adds a ".|." to each side using iteration
    Wtemp = int((width - len(new_pattern)) / 2)  # To work out how many "-"'s are needed to fill width requirement
    new_pattern = ("-" * Wtemp) + new_pattern + ("-" * Wtemp)
    return new_pattern


integers = input().split()
n = int(integers[0])
m = int(integers[1])

remainingN = int((n - 1) / 2)  # Amount of lines above and below the 'WELCOME line'

for i in range(remainingN):
    print(pattern_line(m, i))

print(welcome_line(m))

for i in range(remainingN - 1, -1, -1):
    print(pattern_line(m, i))
