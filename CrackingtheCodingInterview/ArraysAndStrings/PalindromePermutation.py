# 1.4 Given a String write a function to check if its a permutation of a palindrome. THe palindrome doesnt need to be
# limited to just dictionary words.


def PalindromeArray(a):
    a = sorted(a.lower().replace(" ", ""))
    count = 0
    i = 0
    while i < len(a) - 1:
        if a[i] != a[i + 1]:
            count = count + 1
            if (count > 1 and len(a) % 2 == 1) or (count > 0 and len(a) % 2 == 0):
                return False
            i += 1
        else:
            i += 2

    return True


print(PalindromeArray("cacc"))
