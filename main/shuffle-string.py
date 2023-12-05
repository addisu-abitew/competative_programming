class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        orginal_word = ''
        for i in range(len(indices)):
            orginal_word += s[indices.index(i)]
        return orginal_word