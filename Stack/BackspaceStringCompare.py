# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a
# backspace character.
# Example 1:
#
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:
#
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:
#
a = "a##c"
b = "#a#c"


# Output: true
# Explanation: Both S and T become "c".
# Example 4:
#
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# Note:
#
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stackS = []
        stackT = []

        for i in S:
            if i != "#":
                stackS.append(i)
            else:
                if stackS:
                    del (stackS[-1])
        for j in T:
            if j != "#":
                stackT.append(j)
            else:
                if stackT:
                    del (stackT[-1])

        return stackS == stackT
