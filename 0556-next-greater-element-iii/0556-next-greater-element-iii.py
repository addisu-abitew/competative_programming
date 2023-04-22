class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = list(str(n))
        for i in range(len(n)-1,0,-1):
            if int(n[i]) > int(n[i-1]):
                j = -1
                while n[i - 1] >= n[j]:
                    j -= 1
                n[j],n[i -1]  = n[i -1] ,n[j]
                n = n[:i] + n[i:][::-1]
                m = int("".join(n))
                return m if m < 2**31 else -1
        return -1
    