class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        liste = []
        for _ in range(numRows):
            liste.append([])
        nb_dia = 0
        if numRows > 2:
            nb_dia = numRows - 2
        total = numRows + nb_dia
        for index, ele in enumerate(s):
            print(index, ele, index%total)
            if index%(total) >= numRows:
                nb_of_the_dia = index%(total) - numRows
                pos = numRows - 2 - nb_of_the_dia
                print(nb_of_the_dia, pos)
            else:
                pos = index%total
            liste[pos].append(ele)
        print(liste)
        text = ''
        for sub in liste:
            text += ''.join(sub)
        return text

#test
a = Solution()
s = 'PAYPALISHIRING'
numRows = 3
print(a.convert(s, numRows))