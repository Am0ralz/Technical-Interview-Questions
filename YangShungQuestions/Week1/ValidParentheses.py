# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
a = "()"
# Output: true
# Example 2:
#
b = "()[]{}"
# Output: true
# Example 3:
#
c = "(]"
# Output: false
# Example 4:
#
d = "([)]"
# Output: false
# Example 5:
#
e = "{[]}"

f = "}]}()){{)[{[(]"


# Output: true


def isValid(s):
    if len(s) % 2 != 0:
        return False
    lst = []

    for i in s:
        if i == "(" or i == "[" or i == "{":
            lst.append(i)

        elif lst and ((i == ")" and lst[-1] == "(") or (i == "]" and lst[-1] == "[") or (i == "}" and lst[-1] == "{")):
            lst.pop()
        else:
            return False

    return not lst


# print(isValid(a))
# print(isValid(b))
# print(isValid(c))
# print(isValid(d))
# print(isValid(e))
print(isValid(f))
