# 1. 3 Write a method to replace all space in a string with "%20. You may assume that the string has suffiecient space at
# the end for addtional characters


def Urlify(a, b):
    c = ""
    i = 0
    while len(c) != len(a):
        if a[i] == " ":
            c = c + "%20"
        else:
            c = c + a[i]
        i = i + 1
    return c


print(Urlify("Mr John Smith    ", 13))
