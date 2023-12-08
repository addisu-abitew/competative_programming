class Solution:
    def totalMoney(self, n: int) -> int:
        q = n//7
        r = n%7
        full_wks = q*28 + 7*q*(q-1)//2
        rem_wk = r*(r+1)//2 + q*r
        return full_wks + rem_wk