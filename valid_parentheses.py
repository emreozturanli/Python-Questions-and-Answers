# ******VALID PARENTHESES******

# leetcode

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#  1. Open brackets must be closed by the same type of brackets.
#  2. Open brackets must be closed in the correct order.

# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# ANSWER

s = "([()[]{}])"   # YOU CAN CHANGE IT TO WHATEVER YOU WANT TO TRY

for i in range(0,len(s)):
    if "{}" in s or "()" in s or "[]" in s:
        s=s.replace("{}","")
        s=s.replace("()","")
        s=s.replace("[]","")
print(s=="")
