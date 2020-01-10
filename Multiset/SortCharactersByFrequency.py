# Given a string, sort it in decreasing order based on the frequency of characters.
# Example 1:
# Input:
# "tree"
# Output:
# "eert"
#
# Example 2:
# Input:
# "cccaaa"
# Output:
# "cccaaa"
#
# Example 3:
# Input:
t ="Aabb"
# Output:
# "bbAa"
from collections import Counter


from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        cCounter = Counter(s)
        strg = ""
        for i in cCounter.most_common():
            strg += str(i[0])*i[1]
        return strg



