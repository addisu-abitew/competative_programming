class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def typedWord(string):
            arr = []
            for val in string:
                if val == '#':
                    if arr: arr.pop()
                else:
                    arr.append(val)
            return ''.join(arr)
        
        return typedWord(s)==typedWord(t)