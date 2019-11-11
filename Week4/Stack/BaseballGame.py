# You're now a baseball game point recorder.
#
# Given a list of strings, each string can be one of the 4 following types:
#
# Integer (one round's score): Directly represents the number of points you get in this round.
# "+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
# "D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
# "C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
# Each round's operation is permanent and could have an impact on the round before and the round after.
#
# You need to return the sum of the points you could get in all the rounds.
# a = ["5", "2", "C", "D", "+"]


class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        lst = []
        sm = 0
        for i in ops:
            if i == "D":
                sm += (lst[-1] * 2)
                lst.append(lst[-1] * 2)

            elif i == "+":
                num1 = lst.pop()
                num2 = lst.pop()
                sm += num1 + num2
                lst.append(num2)
                lst.append(num1)
                lst.append(num1 + num2)

            elif i == "C":
                sm -= lst.pop()

            else:
                sm += int(i)
                lst.append(int(i))
        return sm