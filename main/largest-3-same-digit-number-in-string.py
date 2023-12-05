class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            req = str(i) * 3
            if req in num:
                return req
        return ''