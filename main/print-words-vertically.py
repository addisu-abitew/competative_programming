class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        hi_len = len(max(words, key=lambda x:len(x)))
        ans = ['' for _ in range(hi_len)]
        for i in range(hi_len):
            for word in words:
                if i < len(word):
                    ans[i] += word[i]
                else:
                    ans[i] += ' '
            ans[i] = ans[i].rstrip()
        return ans