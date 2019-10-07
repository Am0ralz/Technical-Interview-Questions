# We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)
#
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
#
# Return a list of all uncommon words.
#
# You may return the list in any order.
#
# Example 1:
#
A = "this apple is sweet"
B = "this apple is sour"

# Output: ["sweet","sour"]
# Example 2:
#
A = "this apple is sweet"
B = "this apple is sour"



# Output: ["banana"]

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A = (A.split(" "))
        B = (B.split(" "))
        a = set(A)
        b = set(B)
        lst = []
        for i in a.symmetric_difference(b):
            if (A.count(i) + B.count(i)) == 1:
                lst.append(i)

        return lst


