class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        best = 0
        for index in range(len(s)):
            text = ''
            sub_s = s[index:]
            for sub_ele in sub_s:
                if sub_ele not in text:
                    text += sub_ele
                else:
                    break
            if len(text) > best:
                best = len(text)
            if index + best >= len(s):
                break
        return best
        