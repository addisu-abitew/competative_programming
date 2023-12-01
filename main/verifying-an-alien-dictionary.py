class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j] != words[i+1][j]:
                    if order.index(words[i][j]) > order.index(words[i+1][j]): return False
                    break
            if j+1 == len(words[i+1]) and j+1 < len(words[i]) and words[i][j]==words[i+1][j]: return False
        return True