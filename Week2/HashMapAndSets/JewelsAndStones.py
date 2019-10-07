# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
#
# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".
#
# Example 1:
#
# J = "aA"
# S = "aAAbbbb"


# Output: 3
# Example 2:
#
J = "z"
S = "ZZ"


# Output: 0
# Note:
#
# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.


class Solution(object):
    def numJewelsInStones(self, J, S):
        num = 0
        for i in S:
            if i not in set(list(S)).difference(set(list(J))):
                num += 1
        return num



# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
#         jewel_count = 0
#         for j in J:
#             jewel_count += S.count(j)
#         return jewel_count