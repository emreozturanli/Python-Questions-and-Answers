# *********DESIGNER DOOR MAT*********

# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be N x M. (N is an odd natural number, and M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.
# Size: 7 x 21 
   
#   Sample Design:

#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------

# Input Format:

# A single line containing the space separated values of N and M.

# Constraints:
# 5 < N < 101
# 15 < M < 303

# Output Format:

# Output the design pattern.

# Sample Input:

# 9 27

# Sample Output:

#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------


# ANSWER 

N, M = input().split()
N = int(N)
M = int(M)
z = 1
for i in range(N//2):
  print("-"*((M-(3 * z))//2)+".|." * z+"-"*((M-(3 * z))//2))
  z += 2

print("-"*((M-7)//2)+"WELCOME"+"-"*((M-7)//2))
z -= 2
for i in range(N//2):
  print("-"*((M-(3 * z))//2)+".|." * z+"-"*((M-(3 * z))//2))
  z -= 2
