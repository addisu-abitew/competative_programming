class Solution:
    def fib(self, n: int, mem = {0:0, 1:1}) -> int:
        if n not in mem:
            mem[n] = self.fib(n-1) + self.fib(n-2)
        return mem[n]