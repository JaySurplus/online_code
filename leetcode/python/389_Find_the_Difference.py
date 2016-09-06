"""
    389 Find the Difference

    Given two strings s and t which consist of only lowercase letters.

    String t is generated by random shuffling string s and then add one more letter at a random position.

    Find the letter that was added in t.

    Example:

        Input:
            s = "abcd"
            t = "abcde"

        Output:
            e

    Explanation:
        'e' is the letter that was added.
"""
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = 0
        i = 0
        while i < len(s):
            res ^= ord(s[i])
            res ^= ord(t[i])
            i += 1
        res ^= ord(t[i])
        return chr(res)

if __name__ == '__main__':
    sol = Solution()
    s = "abcd"
    t = "abcde"
    res = sol.findTheDifference(s,t)
    print res
