# *****Longest Substring Without Repeating Characters*****

#Leetcode

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


# ANSWER(LEETCODE IDE)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        else:
            substrings = set()
            for i in range(len(s)):
                a = s[i:]
                new_s = ""
                for j in a:
                    if j not in new_s:
                        new_s += j
                        substrings.add(new_s)
                    else:
                        substrings.add(new_s)
                        break
        return len(max(substrings, key=len))

# TRY IT ON YOUR IDE()

s = "abcabcbb"
if s == "":
    print(0)
else:
    substrings = set()
    for i in range(len(s)):
        a = s[i:]
        new_s = ""
        for j in a:
            if j not in new_s:
                new_s += j
                substrings.add(new_s)
            else:
                substrings.add(new_s)
                break
print(len(max(substrings, key=len)))
