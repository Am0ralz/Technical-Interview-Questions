# 1.1 Implement an algorithms to determine if a string has all unique characters

from collections import defaultdict


def isUnique(a):
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                return False
    return True


def isUnique2(a):
    dic = defaultdict(int)
    for i in a:
        if dic[i] == 1:
            return False
        dic[i] = 1
    return True



s = "aplpe"
print(isUnique(s))
print(isUnique2(s))
