#------------------------------------------------------------------------------#
# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.
# Input Format:
#   The first line contains a string, S.
#   The second line contains the width, w.
# Constraints:
#   0 < len(S) < 1000
#   0 < w < len(S)
# Output Format:
#   Print the text wrapped paragraph.
#------------------------------------------------------------------------------#

import textwrap

inputString = input()
width = int(input())

# Converts string into list with 'width' sized chars of same string 
inputString = textwrap.wrap(inputString, width)
for i in inputString:
    print(i)
