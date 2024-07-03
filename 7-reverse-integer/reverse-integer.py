class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = ''
        value = 1
        for i in str(x):
            if i == '-':
                value = -1
            else:
                y += i
        y = value * int(y[::-1])
        if y < -(2 ** 31) or y >(2**31 - 1):
            return 0
        return y
        