class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        extra = 1
        i = len(digits)-1
        while extra and i>=0:
            plus_one = digits[i]+extra
            extra, last = plus_one//10, plus_one%10
            digits[i] = last
            i -= 1
        if extra:
            digits.insert(0, 1)
        return digits