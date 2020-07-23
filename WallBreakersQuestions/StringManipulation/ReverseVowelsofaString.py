# Write a function that takes a string as input and reverse only the vowels of a string.
# Example 1:
#
# Input: "hello"
# Output: "holle"
# Example 2:
#
# Input = "Euston saw I was not Sue."


# Output: "leotcede"

class Solution(object):

    def reverseVowels(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            if s[i].lower() in vowels and s[j].lower() in vowels:
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp
                i += 1
                j -= 1
            elif not s[i] in vowels and not s[j] in vowels :
                j -= 1
                i += 1
            elif not s[i] in vowels:
                i += 1
            elif not s[j] in vowels:
                j -= 1
        return ''.join(s)


print(reverseVowels(Input))
