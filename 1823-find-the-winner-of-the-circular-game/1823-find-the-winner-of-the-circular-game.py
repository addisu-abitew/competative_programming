class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ns = list(range(1, n+1))
        s = 0
        rem = n
        while rem > 1:
            s = (s+k-1)%rem
            ns.pop(s)
            rem -= 1
        return ns[0]