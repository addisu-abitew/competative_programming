class Solution(object):
    def addSpaces(self, s, spaces):
        arr = []
        prev = 0
        for space in spaces:
            arr.append(s[prev:space])
            prev = space
        arr.append(s[space:])
       
        return " ".join(arr)