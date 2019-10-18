# At a lemonade stand, each lemonade costs $5.
#
# Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).
#
# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  You must provide the correct
# change to each customer, so that the net transaction is that the customer pays $5.
#
# Note that you don't have any change in hand at first.
#
# Return true if and only if you can provide every customer with correct change.
# Input = [5, 5, 5, 10, 10, 20]


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        count = 0
        cfive = 0
        for i in bills:
            if i == 5:
                count += 1
            elif count > 0:
                if i == 10:
                    count -= 1
                    cfive += 1
                elif cfive > 0:
                    cfive -= 1
                    count -= 1
                elif count >= 3:
                    count -= 3
                else:
                    return False
            else:
                return False
        return True

