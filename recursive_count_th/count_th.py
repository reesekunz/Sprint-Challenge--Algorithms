'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# 1. Break down problem into smaller sub problems
# 2. String is already sorted so dont need to worry about that
# 3. Need to return total count that, starting at 0, adds 1 everytime the letters "th" are next to each other in the word


def count_th(word):

    thCounter = 0

    if len(word) < 2:
        return 0
    else:
        if "th" in word:
            thCounter = count_th(word[1:]) + 1

    return thCounter


word = "abcthefthghith"
print(count_th(word))


# --------------------------
# if "th" in word:
#     return 1
# else:
#     return 0

# print(word)
# return word

# ----------------------------
# substring = "th"
# count = word.count(substring)

# print ("th count = ", count)
# return count
# ----------------------------

# word = "abcthefthghith"
# print(len(word))
