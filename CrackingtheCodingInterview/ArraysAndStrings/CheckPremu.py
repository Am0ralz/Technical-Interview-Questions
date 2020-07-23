# 1.2 Given two strings write a method to decide if one is a permutation of the other.

def Permu(a, b):
    if len(a) != len(b):
        return False
    a = sorted(a)
    b = sorted(b)
    if a == b:
        return True
    return False


print(Permu("ab", "ba"))
