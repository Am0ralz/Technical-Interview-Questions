# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


def gen_balanced(n):
    table = [['']]
    for j in range(1, n + 1):
        result = []
        for i in range(j):
            for x in table[i]:
                for y in table[j - i - 1]:
                    result.append('(' + x + ')' + y)
        table.append(result)
    return table[n]


print(gen_balanced(3))
