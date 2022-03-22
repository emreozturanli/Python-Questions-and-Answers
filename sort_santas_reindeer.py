# ******* SORT SANTA'S REINDEER ******

#codewars

# Write a function that accepts a sequence of Reindeer names, and returns a sequence with the Reindeer names sorted by their last names.

# Notes:
# It's guaranteed that each string is composed of two words
# In case of two identical last names, keep the original order

# Examples
# For this input: ['Kenjiro Mori', 'Susumu Tokugawa', 'Juzo Okita', 'Akira Sanada']
# Output : ['Kenjiro Mori', 'Juzo Okita', 'Akira Sanada', 'Susumu Tokugawa']

#ANSWER

def sort_reindeer(reindeer_names):
    surnames = []
    output=[]
    for i in reindeer_names:
        a = i.split()
        surnames.append(a[1]) if a[1] not in surnames else None
    for i in sorted(surnames):
        for j in reindeer_names:
            output.append(j) if i in j else None
    return output
