class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        number = list(number)
        i = 0
        for j,n in enumerate(number):
            if n == digit: 
                if j + 1 < len(number) and number[j+1] <= n:
                    i = j
                else:
                    number.pop(j)
                    return ''.join(number)
        number.pop(i)
        return ''.join(number)