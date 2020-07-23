# There are three types of edit that can be performed on strings: insert a character, remove a character or replace
# character. Given two strings write a function to check if they are one edit away.


def Edit(word, editWord):
    if len(word) + 1 > len(editWord) or len(word) - 1 < len(editWord):
        return False
    if len(word) >= len(editWord):
        for i in range(0, len(word)):
            if word[i] != editWord[i]:
                checkWord = word[0:i + 1] + editWord[i + 1:]
                if word == checkWord:
                    return True
    if len(word) < len(editWord):
        for i in range(0, len(word)):
            if word[i] != editWord[i]:
                checkWord = editWord[0:i + 1] + word[i + 1:]
                if editWord == checkWord:
                    return True
                else:
                    return False
        if word == editWord[0:len(word)]:
            return True

    return False
