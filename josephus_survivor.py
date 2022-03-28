# ********JOSEPHUS SURVIVOR********

#codewars

# In this kata you have to correctly return who is the "survivor", ie: the last element of a Josephus permutation.

# Basically you have to assume that n people are put into a circle and that they are eliminated in steps of k elements, like this:

# josephus_survivor(7,3) => means 7 people in a circle;
# one every 3 is eliminated until one remains
# [1,2,3,4,5,6,7] - initial sequence
# [1,2,4,5,6,7] => 3 is counted out
# [1,2,4,5,7] => 6 is counted out
# [1,4,5,7] => 2 is counted out
# [1,4,5] => 7 is counted out
# [1,4] => 5 is counted out
# [4] => 1 counted out, 4 is the last element - the survivor!

#Answer

def josephus_survivor(n,k):
    lst = list(range(1,n+1))
    while len(lst) > 1 :
        if len(lst) >= k :
            lst = lst[k:] + lst[:k-1]
        else:
            i = (k % len(lst)) - 1 
            if i == -1:
                lst = lst[:-1]
            else:
                lst = lst[i+1:] + lst[:i]
    return lst[0]
