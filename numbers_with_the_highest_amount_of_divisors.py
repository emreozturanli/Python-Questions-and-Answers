# ******Numbers with The Highest Amount of Divisors******

# codewars

# An array of different positive integers is given. We should create a code that gives us the number (or the numbers) that has (or have) the highest number of divisors among other data.

# The function proc_arrInt(), (Javascript: procArrInt()) will receive an array of unsorted integers and should output a list with the following results:

# [(1), (2), (3)]

# (1) - Total amount of numbers received (2) - Total prime numbers received (3) - a list [(a), (b)] (a)- The highest amount of divisors that a certain number (or numbers) of the given
# array have (b)- A sorted list with the numbers that have the largest amount of divisors. The list may have only one number.

# Example:
# arr1 = [66, 36, 49, 40, 73, 12, 77, 78, 76, 8, 50, 20, 85, 22, 24, 68, 26, 59, 92, 93, 30]
# proc_arrInt(arr1) ------> [21, 2, [9, [36]]
# 21 integers in the array
# 2 primes: 73 and 97
# 36 is the number that has the highest amount of divisors:
# 1, 2, 3, 4, 6, 9, 12, 18, 36 (9 divisors, including 1 and 36)

# ANSWER

def proc_arrInt(listNum):

    primes = []
    output = [0,[0]]
    maxi = 0
    for i in listNum:
        count = 1
        for j in range(1,(i//2)+1):
            if i % j == 0:
                count += 1
        if count == 2:
            primes.append(i)
        if count > maxi:
            output[0] = count
            output[1] = [i]
            maxi = count
        elif count == maxi:
            output[1].append(i)
            output[1].sort()

    return [len(listNum),len(primes),output]
