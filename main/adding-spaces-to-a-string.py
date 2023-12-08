class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        for i in range(len(spaces)):
            s = s[:i+spaces[i]] + ' ' + s[i+spaces[i]:]
        return s