# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character

# Example 1:
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')


def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    l1, l2 = len(word1), len(word2)
    return minD(word1, word2, l1, l2)


def minD(word1, word2, ln1, ln2):
    if ln1 == 0 and ln2 == 0:
        return 0
    if ln1 > 0 and ln2 == 0:
        return ln1
    if ln1 == 0 and ln2 > 0:
        return ln2

    return min(minD(word1, word2, ln1 - 1, ln2 - 1) + 0 if word1[ln1-1] == word2[ln2-1] else 1, minD(word1, word2, ln1,
                                         ln2 - 1) + 1,
               minD(word1, word2, ln1 - 1, ln2) + 1)
