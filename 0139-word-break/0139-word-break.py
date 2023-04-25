class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        parts = []
        for j in range(1, len(s)+1):
            # print(s[:j], wordDict, parts)
            if s[:j] in wordDict:
                parts.append(j)
                continue
            for i in parts:
                if s[i:j] in wordDict:
                    parts.append(j)
                    break
        return len(s) in parts