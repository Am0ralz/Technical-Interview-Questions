# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.
# Example 1:
#
# Input = "OP"

#//
# Output: true
# Example 2:
#
# Input: "race a car"
# Output: false


class Solution(object):

    def isPalindrome(self, s):
        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z', '0', '1', '2', '3' , '4', '5' ,'6' ,'7' ,'8', '9']
        s = s.lower()
        for i in s:
            if i not in chars:
                s = s.replace(i, "")
        if s == s[::-1]:
            return True
        else:
            return False
