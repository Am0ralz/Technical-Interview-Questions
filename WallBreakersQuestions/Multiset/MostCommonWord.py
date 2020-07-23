# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
#
# Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.
# Input:
p = "Bob hit a ball, the hit BALL flew far after it was hit."
b = ["hit"]
d = "abc abc? abcd the jeff!"
c = ["abc", "abcd", "jeff"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.
# from collections import Counter
# import string


from collections import Counter
import string


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        for i in string.punctuation:
            if i in paragraph:
                paragraph = paragraph.replace(i, " ")
        paragraph = paragraph.split()
        if banned:
            for i in banned:
                while i in paragraph:
                    paragraph.remove(i)

        cCounter = Counter(paragraph)

        return cCounter.most_common(1)[0][0]

# paragraph = paragraph.lower()
# for i in string.punctuation:
#     if i in paragraph:
#         paragraph = paragraph.replace(i, " ")
# paragraph = paragraph.split()
# if banned:
#     for i in banned:
#         while i in paragraph:
#             paragraph.remove(i)
#
# cCounter = Counter(paragraph)
#
# return cCounter.most_common(1)[0][0]
