class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        nb = ''
        moins = 1
        for i in str(x)[::-1]:
            if i == '-':
                moins = -1
            else:
                nb += i
        if moins == -1:
            if int(nb) > 2**31:
                return 0
        else:
            if int(nb) > 2**31 - 1:
                return 0
        return int(nb)*moins
    
#test
a = Solution()
x = -123
print(a.reverse(x))