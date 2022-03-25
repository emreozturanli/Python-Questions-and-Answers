# ********GROUP ANAGRAMS********

# leetcode

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:

# Input: strs = [""]
# Output: [[""]]

# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

#ANSWER

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = []
        sorted_set=set()
        dic = {}
        for i in range(len(strs)):
            sorted_list.append("".join(sorted(strs[i])))
        sorted_set = set(sorted_list)
        for i in sorted_set:
            dic[i]=[]
        for i in strs:
            if ("".join(sorted(i))) in dic.keys():
                dic["".join(sorted(i))] += [i]
            else:
                dic["".join(sorted(i))] += [i]
        return list(dic.values())

#TRY IT ON YOUR IDE

strs = ["eat","tea","tan","ate","nat","bat"] 
sorted_list = []
sorted_set=set()
dic = {}
for i in range(len(strs)):
    sorted_list.append("".join(sorted(strs[i])))
sorted_set = set(sorted_list)
for i in sorted_set:
    dic[i]=[]
for i in strs:
    if ("".join(sorted(i))) in dic.keys():
        dic["".join(sorted(i))] += [i]
    else:
        dic["".join(sorted(i))] += [i]
print(list(dic.values()))
