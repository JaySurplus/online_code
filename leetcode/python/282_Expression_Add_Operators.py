"""
    282. Expression Add Operators
    Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

    Examples:
        "123", 6 -> ["1+2+3", "1*2*3"]
        "232", 8 -> ["2*3+2", "2+3*2"]
        "105", 5 -> ["1*0+5","10-5"]
        "00", 0 -> ["0+0", "0-0", "0*0"]
        "3456237490", 9191 -> []

"""


class Solution(object):

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not target:
            return None
        res = []
        temp = ""
        index = 0
        helper(res, temp, index , target)
        return res

    def helper(self, res, temp, index ,target):



