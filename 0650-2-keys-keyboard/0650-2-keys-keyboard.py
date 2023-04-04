class Solution(object):
    def minSteps(self, n):
        if n == 1: return 0
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        isComposite = False
        for i in prime_numbers:
            if n % i == 0:
                isComposite = True
                break
        if not isComposite:
            return n
        prime_factors = []
        while n > 1:
            for div in prime_numbers:
                if n % div == 0:
                    prime_factors.append(div)
                    n //= div
                    break
            else:
                prime_factors.append(n)
                break
        return sum(prime_factors)