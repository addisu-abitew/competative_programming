class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2: 
            return False
        count1 = Counter(s1)
        count2 = Counter(s2[:n1-1])
        for left in range(len(s2)-len(s1)+1):
            right = left + n1-1
            count2[s2[right]] += 1
            if count1 == count2:
                return True
            count2[s2[left]] -= 1
        return False