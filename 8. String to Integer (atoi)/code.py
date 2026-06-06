class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 1
        sign = 1
        nb = 0
        if len(s) < 1:
            return 0
        if s[0] == ' ':
            return self.myAtoi(s[1:])
        elif s[0] == '-':
            sign = -1
        elif s[0] == '+':
            sign = 1
        else:
            start = 0
        for i in s[start:]:
            if i in '1234567890':
                nb *= 10
                nb += int(i)
            else:
                break
        nb *= sign
        if nb < -2**31:
            nb = -2**31
        elif nb >= 2**31:
            nb = 2**31 - 1
        return nb

#test
a = Solution()
s = " -042C8"
print(a.myAtoi(s))