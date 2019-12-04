# Given a chemical formula (given as a string), return the count of each atom.
#
# An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the
# name.
#
# 1 or more digits representing the count of that element may follow if the count is greater than 1. If the count is
# 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.
#
# Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.
#
# A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3
# are formulas.
#
# Given a formula, output the count of all elements as a string in the following form: the first name (in sorted
# order), followed by its count (if that count is more than 1), followed by the second name (in sorted order),
# followed by its count (if that count is more than 1), and so on.
import re
from collections import defaultdict
from itertools import chain


def countOfAtoms(self, formula):
    dict = defaultdict(int)
    count_rec(formula, dict)
    return ''.join(chain.from_iterable(
        [[atom, str(dict[atom]) if dict[atom] > 1 else ''] for atom in sorted(dict.keys())]))


def count_rec( formula, res):
    if formula is None or len(formula) == 0:
        return
    if formula[0] == '(':
        count, i = 1, 1
        while count != 0:
            if formula[i] == '(': count += 1
            if formula[i] == ')': count -= 1
            i += 1
        temp_res = defaultdict(int)
        count_rec(formula[1:i - 1], temp_res)
        num = re.findall('^\d+', formula[i:])
        if len(num) > 0:
            num = int(num[0])
            i += len(str(num))
        else:
            num = 1
        for atom in temp_res:
            res[atom] += temp_res[atom] * num
        count_rec(formula[i:], res)
    else:
        atom = re.findall('[A-Z][a-z]*', formula)[0]
        num = re.findall('^\d+', formula[len(atom):])
        num = int(num[0]) if len(num) > 0 else 1
        res[atom] += num
        count_rec(formula[len(atom) + (0 if num == 1 else len(str(num))):], res)
