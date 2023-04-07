class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = self.sn(n, {})
        return s[k-1]
            
    def sn(self,n, mem):
        if n == 0: return "0"
        if n not in mem: mem[n] = self.sn(n-1,mem)
        return mem[n] + "1" + self.rev(self.invert(mem[n]))
      
    def invert(self,s):
        res = ""
        for i in s: 
            if i == "0":
                res += "1"
            else:
                res += "0"
        return res
    def rev(self,s):
        return s[::-1]
        
        