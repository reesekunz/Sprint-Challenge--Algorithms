'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# PLANNING:
# BASE CASE - when are we done? When the length of the word is less than 2 letters, we know there can't be anymore cases.
# RECURSIVE CASE - What are we trying to return? Number of times "th" occurs within a word.
# How do we get to base case? Removing front of index after comparing first two indexes. Continue until length of word is less than 2.


def count_th(word):
    # print("first two letters = ", word[:2])
    # BASE CASE
    if len(word) < 2:
        return 0

    # RECURSIVE CASE
    # If first two indexes contain 'th", add one to the count - skip over the first index and compare next two adjacent indexes
    elif word[:2] == "th":
        return count_th(word[1:]) + 1
    # If first two indexes dont contain 'th', just skip over the first index and compare next two adjacent indexes
    else:
        # print("count th return", count_th(word[1:]))
        return count_th(word[1:])
