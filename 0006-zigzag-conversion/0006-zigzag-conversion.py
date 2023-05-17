class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows<=1: return s
        sol = ''
        for i in range(numRows):
            j = 0
            if i>0 and i<numRows-1:
                j = i + 2*(numRows-i-1)
            while i<len(s):
                sol += s[i]
                if j and j<len(s):
                    sol += s[j]
                    j += 2*(numRows-1)
                i += 2*(numRows-1)
        return sol