class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        stack = []
        for n in num :
            while stack and int(stack[-1]) > int(n) and k:
                stack.pop()
                k -= 1
            stack.append(n)
            
        while k:
            stack.pop()
            k -= 1
        return str(int(''.join(stack)))
                
        
                
        