class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.index(needle) if needle in haystack else -1