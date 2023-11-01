class Solution:
    def pivotInteger(self, n: int) -> int:
        presum = [0]
        for num in range(1, n+1):
            presum.append(presum[-1] + num)
        for i in range(1, n+1):
            if presum[i] == presum[-1]-presum[i-1]:
                return i
        return -1