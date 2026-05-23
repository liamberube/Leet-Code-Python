class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        best = s[0], 1
        alphabet = ''
        for i in s:
            if i not in alphabet:
                alphabet += i
        for letter in alphabet:
            list_pos = []
            for index in range(len(s)):
                if s[index] == letter:
                    list_pos.append(index)
            lenght = len(list_pos)
            if lenght <= 1:
                continue
            else:
                for i in range(lenght):
                    for j in range(i + 1, lenght):
                        new = s[list_pos[i]:list_pos[j] + 1]
                        if new == new[::-1]:
                            if len(new) > best[1]:
                                best = new, len(new)
        return best[0]

#test
a = Solution()
s = "cbbd"
print(a.longestPalindrome(s))