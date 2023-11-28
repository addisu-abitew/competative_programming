class Solution:
    def isPalindrome(self, x: int) -> bool:
        def reverse(num):
            rev = 0
            while num > 0:
                rev = rev*10 + num%10
                num //= 10
            return rev
        
        return x == reverse(x)