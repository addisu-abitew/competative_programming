class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_len =0
        l=0
        count = 0
        for r in range(len(s)):
            if s[r] in "aeiou":
                count+=1

            if r>=k-1:
                max_len= max(count,max_len)
                if s[l] in "aeiou":
                    count-=1
                l+=1
        return max_len