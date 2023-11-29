class Solution(object):
    def longestCommonPrefix(self, strs):
        common = strs[0]
        for word in strs:
            if len(word) == 0: return ''
            for i in range(len(word)):
                if i<len(common) and common[i] != word[i]:
                    common = common[:i]
                if i<len(common) and (i+1) == len(word) and common[i] == word[i]:
                    common = word
        return common